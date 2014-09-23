import json
import datetime

from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.db import models

from .node import Node
from .graph import Graph


class Edge(models.Model):

    """
    Class: Edge

    Models a generic edge for any diagram notation that connects two nodes with each other.

    Attributes:
     {long}   client_id  - the id of the edge as generated by the client
     {<Node>} source     - starting point of the edge
     {<Node>} target     - endpoint of the edge
     {bool}   deleted    - flag indicating whether the edge was deleted. Simplifies the restoration of the edge by
                           toggling this switch.
    """
    class Meta:
        app_label = 'FuzzEd'

    client_id = models.BigIntegerField()
    graph = models.ForeignKey(Graph, null=False, related_name='edges')
    source = models.ForeignKey(Node, null=False, related_name='outgoing')
    target = models.ForeignKey(Node, null=False, related_name='incoming')
    deleted = models.BooleanField(default=False)
    # TODO: maybe add a reference to the graph. this would simplify the
    # JSON-serialization of the graph

    def __unicode__(self):
        prefix = '[DELETED] ' if self.deleted else ''
        return unicode('%s%s -> %s' %
                       (prefix, str(self.source), str(self.target)))

    def to_dict(self, use_value_dict=False):
        """
        Method: to_dict

        Represents this edge as a native dictionary

        Returns:
         {dict} the edge as dictionary
        """
        if use_value_dict:
            prop_values = {prop.key: {'value': prop.value}
                           for prop in self.properties.filter(deleted=False)}
        else:
            prop_values = {
                prop.key: prop.value for prop in self.properties.filter(
                    deleted=False)}

        return {
            'properties': prop_values,
            'id': self.client_id,
            'graph': self.graph.pk,
            'source': self.source.client_id,
            'target': self.target.client_id
        }

    def to_graphml(self):
        """
        Method: to_graphml

        Serializes this edge instance to its graphml representation

        Returns:
         {str} the edge in graphml
        """
        return '       <edge source="%s" target="%s" />\n' % (
            self.source.client_id, self.target.client_id,)

    def to_json(self, use_value_dict=False):
        """
        Method: to_json

        Serializes the values of the edge into a python dictionary that is JSON conform.

        Returns:
         {dict} the edge as dictionary
        """
        return json.dumps(self.to_dict(use_value_dict))

    def set_attr(self, key, value):
        """
        Method: set_attr

        Use this method to set a edge's attribute. It looks in the edge object and its related properties for an
        attribute with the given name and changes it. If non exist, a new property is added saving this attribute.

        Parameters:
            {string} key - The name of the attribute.
            {attr} value - The new value that should be stored.

        TODO: Deprecate this method, set_attrs() should only be used to have an efficient modification signal handling.
        """
        assert(self.pk)
        from FuzzEd.models import Property
        if hasattr(self, key):
            # Native Edge attribute, such as client_id
            setattr(self, key, value)
        else:
            prop, created = self.properties.get_or_create(
                key=key, defaults={
                    'edge': self})
            prop.save_value(value)

    def set_attrs(self, d):
        '''
            Set edge attributes according to the provided dictionary.

            TODO: Replace by true bulk insert implementation.
        '''
        for key, value in d.iteritems():
            self.set_attr(key, value)
        post_save.send(sender=self.__class__, instance=self)


@receiver(post_save, sender=Edge)
@receiver(pre_delete, sender=Edge)
def graph_modify(sender, instance, **kwargs):
    instance.graph.modified = datetime.datetime.now()
    instance.graph.save()
    # updating project modification date
    instance.graph.project.modified = instance.graph.modified
    instance.graph.project.save()
