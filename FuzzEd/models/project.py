from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver



class Project(models.Model):
  """
  Class: Project
  
  Fields:
   {str}            name     - the name of the project
   {User}           owner    - a link to the owner of the project
   {const datetime} created  - timestamp of the moment of project creation (default: now)
   {bool}           deleted  - flag indicating whether this project was deleted or not. Simplifies restoration of the
                               project if needed by toggling this member (default: False)
  """
  
  class Meta:
      app_label = 'FuzzEd'
  
  name      = models.CharField(max_length=255)
  owner     = models.ForeignKey(User, related_name='own_projects')
  users     = models.ManyToManyField(User, related_name='projects')
  
  created   = models.DateTimeField(auto_now_add=True, editable=False)
  deleted   = models.BooleanField(default=False)
  
  def to_dict(self):
      """
      Method: to_dict
      
      Encodes the project as dictionary 
      
      Returns:
       {dict} the project as dictionary
      """
      return {
          'pk':       self.pk,
          'name':     self.name,
          'created':  self.created
      }
  
  