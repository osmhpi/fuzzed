# DO NOT EDIT ! This file is autogenerated by 'setup.py build'

notations=[{u'kind': u'faulttree', u'name': u'Fault Tree', u'propertiesDisplayOrder': [u'name', u'probability', u'kN', u'cardinality'], u'defaults': {u'nodes': [{u'y': 1, u'x': 10, u'kind': u'topEvent'}]}, u'nodes': {u'node': {u'numberOfIncomingConnections': 1, u'connector': {u'offset': {u'top': 0, u'bottom': 0}}, u'allowConnectionTo': [u'node'], u'numberOfOutgoingConnections': -1, u'deletable': True}, u'topEvent': {u'inherits': u'event', u'excludeFromShapesMenu': True, u'name': u'Top Event', u'numberOfOutgoingConnections': 1, u'propertyMenuEntries': {u'optional': None}, u'image': u'top_event.svg', u'numberOfIncomingConnections': 0, u'deletable': False, u'optional': None}, u'votingOrGate': {u'inherits': u'gate', u'name': u'Voting OR Gate', u'propertyMenuEntries': {u'kN': {u'kind': u'range', u'displayName': u'k-out-of-N', u'step': 1, u'min': 1}}, u'image': u'voting_or_gate.svg', u'kN': [1, 2], u'propertyMirrors': {u'kN': {u'position': u'bottom', u'style': [u'italic'], u'prefix': u'k/N: '}}, u'help': u'Output event occurs if the given number of input events occur'}, u'orGate': {u'inherits': u'gate', u'connector': {u'offset': {u'bottom': -7}}, u'image': u'or_gate.svg', u'name': u'OR Gate', u'help': u'Output event occurs if one or more input events occur'}, u'basicEvent': {u'inherits': u'event', u'numberOfOutgoingConnections': 0, u'name': u'Basic Event', u'probability': 0, u'propertyMenuEntries': {u'probability': {u'disabled': False, u'max': 1, u'kind': u'number', u'step': 0.01, u'min': 0}}, u'image': u'basic_event.svg', u'propertyMirrors': {u'probability': {u'position': u'bottom', u'style': [u'italic'], u'prefix': u'p='}}, u'help': u'Initiating failure in a basic component'}, u'intermediateEventSet': {u'inherits': u'intermediateEvent', u'name': u'Intermediate Event Set', u'propertyMenuEntries': {u'cardinality': {u'kind': u'number', u'displayName': u'Cardinality', u'step': 1, u'min': 1}}, u'image': u'intermediate_event_set.svg', u'propertyMirrors': {u'cardinality': {u'position': u'bottom', u'style': [u'italic'], u'prefix': u'#'}}, u'cardinality': 1, u'help': u'Set of intermediate events'}, u'andGate': {u'inherits': u'gate', u'image': u'and_gate.svg', u'name': u'AND Gate', u'help': u'Output event occurs if all input events occur'}, u'xorGate': {u'inherits': u'gate', u'image': u'xor_gate.svg', u'name': u'XOR Gate', u'help': u'Output event occurs if exactly one of the input events occur'}, u'undevelopedEvent': {u'inherits': u'event', u'image': u'undeveloped_event.svg', u'name': u'Undeveloped Event', u'numberOfOutgoingConnections': 0, u'help': u'Event with no information available or insignificant impact'}, u'gate': {u'inherits': u'node'}, u'basicEventSet': {u'inherits': u'basicEvent', u'name': u'Basic Event Set', u'propertyMenuEntries': {u'cardinality': {u'kind': u'number', u'displayName': u'Cardinality', u'step': 1, u'min': 1}}, u'image': u'basic_event_set.svg', u'propertyMirrors': {u'cardinality': {u'position': u'bottom', u'style': [u'italic'], u'prefix': u'#'}}, u'cardinality': 1, u'help': u'Set of basic events with identical properties'}, u'intermediateEvent': {u'inherits': u'event', u'image': u'intermediate_event.svg', u'help': u'Failure resulting from a combination of previous events', u'allowConnectionTo': [u'gate', u'basicEvent'], u'name': u'Intermediate Event'}, u'event': {u'inherits': u'node', u'propertyMenuEntries': {u'name': {u'kind': u'text', u'displayName': u'Name'}, u'probability': {u'disabled': True, u'kind': u'text', u'displayName': u'Probability'}}, u'propertyMirrors': {u'name': {u'position': u'bottom', u'style': [u'bold', u'large']}}, u'allowConnectionTo': [u'gate'], u'probability': 0}, u'houseEvent': {u'inherits': u'event', u'image': u'house_event.svg', u'name': u'House Event', u'numberOfOutgoingConnections': 0, u'help': u'An event that is expected to occur and typically does not denote a failure'}}, u'shapeMenuNodeDisplayOrder': [u'basicEvent', u'basicEventSet', u'intermediateEvent', u'intermediateEventSet', u'andGate', u'orGate', u'xorGate', u'votingOrGate', u'undevelopedEvent', u'houseEvent', u'topEvent']}, {u'kind': u'fuzztree', u'name': u'Fuzz Tree', u'propertiesDisplayOrder': [u'name', u'cost', u'probability', u'optional', u'kN', u'cardinality', u'kFormula', u'nRange', u'decompositions'], u'defaults': {u'nodes': [{u'y': 1, u'x': 10, u'kind': u'topEvent'}]}, u'nodes': {u'node': {u'numberOfIncomingConnections': 1, u'numberOfOutgoingConnections': -1, u'allowConnectionTo': [u'node'], u'connector': {u'offset': {u'top': 0, u'bottom': 0}}, u'deletable': True, u'optional': None}, u'topEvent': {u'inherits': u'event', u'excludeFromShapesMenu': True, u'name': u'Top Event', u'numberOfOutgoingConnections': 1, u'propertyMenuEntries': {u'optional': None, u'decompositions': {u'kind': u'number', u'displayName': u'Decompose', u'step': 1, u'min': 1}}, u'image': u'top_event.svg', u'numberOfIncomingConnections': 0, u'deletable': False, u'decompositions': 1, u'optional': None}, u'variationPoint': {u'inherits': u'node', u'propertyMenuEntries': {u'name': {u'kind': u'text', u'displayName': u'Name'}}, u'propertyMirrors': {u'name': {u'position': u'bottom', u'style': [u'bold', u'large']}}}, u'votingOrGate': {u'inherits': u'gate', u'name': u'Voting OR Gate', u'propertyMenuEntries': {u'kN': {u'kind': u'range', u'displayName': u'k-out-of-N', u'step': 1, u'min': 1}}, u'image': u'voting_or_gate.svg', u'kN': [1, 2], u'propertyMirrors': {u'kN': {u'position': u'bottom', u'style': [u'italic'], u'prefix': u'k/N: '}}, u'help': u'Output event occurs if the given number of input events occur'}, u'orGate': {u'inherits': u'gate', u'connector': {u'offset': {u'bottom': -7}}, u'image': u'or_gate.svg', u'name': u'OR Gate', u'help': u'Output event occurs if one or more input events occur'}, u'intermediateEvent': {u'inherits': u'event', u'help': u'Failure resulting from a combination of previous events', u'propertyMenuEntries': {u'cost': None}, u'image': u'intermediate_event.svg', u'allowConnectionTo': [u'gate', u'basicEvent'], u'cost': None, u'propertyMirrors': {u'cost': None}, u'name': u'Intermediate Event'}, u'intermediateEventSet': {u'inherits': u'intermediateEvent', u'name': u'Intermediate Event Set', u'propertyMenuEntries': {u'cardinality': {u'kind': u'number', u'displayName': u'Cardinality', u'step': 1, u'min': 1}, u'cost': None}, u'image': u'intermediate_event_set.svg', u'propertyMirrors': {u'cardinality': {u'position': u'bottom', u'style': [u'italic'], u'prefix': u'#'}, u'cost': None}, u'cardinality': 1, u'help': u'Set of intermediate events'}, u'featureVariation': {u'inherits': u'variationPoint', u'changedChildProperties': {u'optional': None}, u'help': u'Placeholder for one of the input events', u'image': u'feature_variation.svg', u'allowConnectionTo': [u'intermediateEvent'], u'connector': {u'dashstyle': u'4 2'}, u'name': u'Feature Variation'}, u'andGate': {u'inherits': u'gate', u'image': u'and_gate.svg', u'name': u'AND Gate', u'help': u'Output event occurs if all input events occur'}, u'xorGate': {u'inherits': u'gate', u'image': u'xor_gate.svg', u'name': u'XOR Gate', u'help': u'Output event occurs if exactly one of the input events occur'}, u'redundancyVariation': {u'inherits': u'variationPoint', u'nRange': [1, 2], u'help': u'Placeholder for a voting OR gate over a chosen number of the input events', u'numberOfOutgoingConnections': 1, u'propertyMenuEntries': {u'kFormula': {u'kind': u'text', u'displayName': u'K-Formula'}, u'nRange': {u'kind': u'range', u'displayName': u'N-Range', u'step': 1, u'min': 1}}, u'image': u'redundancy_variation.svg', u'kFormula': u'N-2', u'allowConnectionTo': [u'intermediateEventSet', u'basicEventSet'], u'connector': {u'dashstyle': u'4 2'}, u'changedChildProperties': {u'optional': None}, u'propertyMirrors': {u'kFormula': {u'position': u'bottom', u'style': [u'italic'], u'prefix': u'k: '}, u'nRange': {u'position': u'bottom', u'style': [u'italic'], u'prefix': u'N: '}}, u'name': u'Redundancy Variation'}, u'undevelopedEvent': {u'inherits': u'event', u'image': u'undeveloped_event.svg', u'name': u'Undeveloped Event', u'numberOfOutgoingConnections': 0, u'help': u'Event with no information available or insignificant impact'}, u'gate': {u'inherits': u'node'}, u'basicEventSet': {u'inherits': u'basicEvent', u'name': u'Basic Event Set', u'propertyMenuEntries': {u'cardinality': {u'kind': u'number', u'displayName': u'Cardinality', u'step': 1, u'min': 1}}, u'image': u'basic_event_set.svg', u'propertyMirrors': {u'cardinality': {u'position': u'bottom', u'style': [u'italic'], u'prefix': u'#'}}, u'cardinality': 1, u'help': u'Set of basic events with identical properties'}, u'basicEvent': {u'inherits': u'event', u'numberOfOutgoingConnections': 0, u'name': u'Basic Event', u'probability': [0.5, 0], u'propertyMenuEntries': {u'probability': {u'disabled': False, u'kind': u'compound', u'defaults': {u'Fuzzy': [0.5, 0.3], u'Exact': [0.5, 0]}, u'choices': {u'Fuzzy': {u'kind': u'select', u'values': {u'very likely': [0.8, 0.1], u'more or less': [0.5, 0.3], u'never': [0, 0], u'likely': [0.66, 0.2], u'very unlikely': [0.2, 0.1], u'unlikely': [0.33, 0.2], u'always': [1, 0]}, u'choices': [u'never', u'very unlikely', u'unlikely', u'more or less', u'likely', u'very likely', u'always']}, u'Exact': {u'kind': u'neighborhood', u'min': 0, u'max': 1, u'epsilonMax': 1, u'epsilonMin': 0, u'step': 0.0001, u'epsilonStep': 0.0001}}}}, u'image': u'basic_event.svg', u'probabilitySelected': u'Exact', u'propertyMirrors': {u'probability': {u'position': u'bottom', u'style': [u'italic'], u'prefix': u'p='}}, u'help': u'Initiating failure in a basic component'}, u'event': {u'inherits': u'node', u'probability': 0, u'propertyMenuEntries': {u'cost': {u'disabled': True, u'kind': u'number', u'displayName': u'Cost', u'step': 1, u'min': 0}, u'optional': {u'kind': u'checkbox', u'displayName': u'Optional'}, u'name': {u'kind': u'text', u'displayName': u'Name'}, u'probability': {u'disabled': True, u'kind': u'text', u'displayName': u'Probability'}}, u'allowConnectionTo': [u'gate'], u'cost': 1, u'propertyMirrors': {u'name': {u'position': u'bottom', u'style': [u'bold', u'large']}}, u'optional': False}, u'houseEvent': {u'inherits': u'event', u'image': u'house_event.svg', u'name': u'House Event', u'numberOfOutgoingConnections': 0, u'help': u'An event that is expected to occur and typically does not denote a failure'}}, u'shapeMenuNodeDisplayOrder': [u'basicEvent', u'basicEventSet', u'intermediateEvent', u'intermediateEventSet', u'andGate', u'orGate', u'xorGate', u'votingOrGate', u'undevelopedEvent', u'featureVariation', u'redundancyVariation', u'houseEvent', u'topEvent']}, {u'kind': u'rbd', u'name': u'Reliability Block Diagram', u'propertiesDisplayOrder': [u'name', u'probability', u'out_of'], u'defaults': {u'nodes': [{u'y': 1, u'x': 5, u'kind': u'start'}, {u'y': 1, u'x': 10, u'kind': u'end'}]}, u'nodes': {u'node': {u'numberOfIncomingConnections': -1, u'name': u'Node', u'numberOfOutgoingConnections': -1, u'propertyMenuEntries': {u'name': {u'kind': u'text', u'displayName': u'Name'}}, u'allowConnectionTo': [], u'connector': {u'offset': {u'top': 0, u'bottom': 0}}, u'propertyMirrors': {u'name': {u'position': u'bottom', u'style': [u'bold', u'large']}}}, u'start': {u'inherits': u'node', u'numberOfIncomingConnections': 0, u'name': u'Start', u'image': u'start.svg', u'excludeFromShapesMenu': True, u'allowConnectionTo': [u'end', u'block', u'out_of'], u'connector': {u'offset': {u'right': -9.1}}, u'deletable': False}, u'out_of': {u'inherits': u'node', u'excludeFromShapesMenu': False, u'name': u'Out of', u'numberOfOutgoingConnections': 1, u'propertyMenuEntries': {u'out_of': {u'kind': u'range', u'displayName': u'Out of', u'step': 1, u'min': 1}}, u'image': u'out_of.svg', u'allowConnectionTo': [u'block', u'end'], u'propertyMirrors': {u'out_of': {u'position': u'bottom', u'style': [u'italic']}}, u'out_of': [1, 1]}, u'end': {u'inherits': u'node', u'excludeFromShapesMenu': True, u'name': u'End', u'numberOfOutgoingConnections': 0, u'image': u'end.svg', u'connector': {u'offset': {u'left': 8.1}}, u'deletable': False}, u'block': {u'inherits': u'node', u'excludeFromShapesMenu': False, u'name': u'Block', u'probability': 0, u'propertyMenuEntries': {u'probability': {u'kind': u'number', u'displayName': u'Probability', u'min': 0, u'max': 1, u'disabled': False, u'step': 0.01}}, u'image': u'block.svg', u'allowConnectionTo': [u'end', u'block', u'out_of'], u'propertyMirrors': {u'probability': {u'position': u'bottom', u'style': [u'italic'], u'prefix': u'p='}}}}, u'shapeMenuNodeDisplayOrder': [u'block', u'out_of', u'start', u'end']}]