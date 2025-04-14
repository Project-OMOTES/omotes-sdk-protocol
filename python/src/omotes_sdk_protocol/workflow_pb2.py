# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: omotes_sdk_protocol/workflow.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"omotes_sdk_protocol/workflow.proto\"4\n\nStringEnum\x12\x10\n\x08key_name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\"V\n\x0fStringParameter\x12\x14\n\x07\x64\x65\x66\x61ult\x18\x01 \x01(\tH\x00\x88\x01\x01\x12!\n\x0c\x65num_options\x18\x02 \x03(\x0b\x32\x0b.StringEnumB\n\n\x08_default\"4\n\x10\x42ooleanParameter\x12\x14\n\x07\x64\x65\x66\x61ult\x18\x01 \x01(\x08H\x00\x88\x01\x01\x42\n\n\x08_default\"x\n\x10IntegerParameter\x12\x14\n\x07\x64\x65\x66\x61ult\x18\x01 \x01(\x03H\x00\x88\x01\x01\x12\x14\n\x07minimum\x18\x02 \x01(\x03H\x01\x88\x01\x01\x12\x14\n\x07maximum\x18\x03 \x01(\x03H\x02\x88\x01\x01\x42\n\n\x08_defaultB\n\n\x08_minimumB\n\n\x08_maximum\"v\n\x0e\x46loatParameter\x12\x14\n\x07\x64\x65\x66\x61ult\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12\x14\n\x07minimum\x18\x02 \x01(\x02H\x01\x88\x01\x01\x12\x14\n\x07maximum\x18\x03 \x01(\x02H\x02\x88\x01\x01\x42\n\n\x08_defaultB\n\n\x08_minimumB\n\n\x08_maximum\"5\n\x11\x44\x61teTimeParameter\x12\x14\n\x07\x64\x65\x66\x61ult\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\n\n\x08_default\"y\n\x11\x44urationParameter\x12\x14\n\x07\x64\x65\x66\x61ult\x18\x02 \x01(\x02H\x00\x88\x01\x01\x12\x14\n\x07minimum\x18\x03 \x01(\x02H\x01\x88\x01\x01\x12\x14\n\x07maximum\x18\x04 \x01(\x02H\x02\x88\x01\x01\x42\n\n\x08_defaultB\n\n\x08_minimumB\n\n\x08_maximum\"\x8e\x05\n\x11WorkflowParameter\x12\x10\n\x08key_name\x18\x01 \x01(\t\x12\x12\n\x05title\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x18\n\x0b\x64\x65scription\x18\x03 \x01(\tH\x02\x88\x01\x01\x12,\n\x10string_parameter\x18\x04 \x01(\x0b\x32\x10.StringParameterH\x00\x12.\n\x11\x62oolean_parameter\x18\x05 \x01(\x0b\x32\x11.BooleanParameterH\x00\x12.\n\x11integer_parameter\x18\x06 \x01(\x0b\x32\x11.IntegerParameterH\x00\x12*\n\x0f\x66loat_parameter\x18\x07 \x01(\x0b\x32\x0f.FloatParameterH\x00\x12\x30\n\x12\x64\x61tetime_parameter\x18\x08 \x01(\x0b\x32\x12.DateTimeParameterH\x00\x12\x30\n\x12\x64uration_parameter\x18\t \x01(\x0b\x32\x12.DurationParameterH\x00\x12\x32\n\x0b\x63onstraints\x18\n \x03(\x0b\x32\x1d.WorkflowParameter.Constraint\x1a\xba\x01\n\nConstraint\x12\x16\n\x0eother_key_name\x18\x01 \x01(\t\x12<\n\x08relation\x18\x02 \x01(\x0e\x32*.WorkflowParameter.Constraint.RelationType\"V\n\x0cRelationType\x12\x0b\n\x07GREATER\x10\x00\x12\x11\n\rGREATER_OR_EQ\x10\x01\x12\x0b\n\x07SMALLER\x10\x02\x12\x11\n\rSMALLER_OR_EQ\x10\x03\x12\x06\n\x02\x45Q\x10\x04\x42\x10\n\x0eparameter_typeB\x08\n\x06_titleB\x0e\n\x0c_description\"_\n\x08Workflow\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12\x18\n\x10type_description\x18\x02 \x01(\t\x12&\n\nparameters\x18\x03 \x03(\x0b\x32\x12.WorkflowParameter\"2\n\x12\x41vailableWorkflows\x12\x1c\n\tworkflows\x18\x01 \x03(\x0b\x32\t.Workflow\"\x1b\n\x19RequestAvailableWorkflowsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'omotes_sdk_protocol.workflow_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_STRINGENUM']._serialized_start=38
  _globals['_STRINGENUM']._serialized_end=90
  _globals['_STRINGPARAMETER']._serialized_start=92
  _globals['_STRINGPARAMETER']._serialized_end=178
  _globals['_BOOLEANPARAMETER']._serialized_start=180
  _globals['_BOOLEANPARAMETER']._serialized_end=232
  _globals['_INTEGERPARAMETER']._serialized_start=234
  _globals['_INTEGERPARAMETER']._serialized_end=354
  _globals['_FLOATPARAMETER']._serialized_start=356
  _globals['_FLOATPARAMETER']._serialized_end=474
  _globals['_DATETIMEPARAMETER']._serialized_start=476
  _globals['_DATETIMEPARAMETER']._serialized_end=529
  _globals['_DURATIONPARAMETER']._serialized_start=531
  _globals['_DURATIONPARAMETER']._serialized_end=652
  _globals['_WORKFLOWPARAMETER']._serialized_start=655
  _globals['_WORKFLOWPARAMETER']._serialized_end=1309
  _globals['_WORKFLOWPARAMETER_CONSTRAINT']._serialized_start=1079
  _globals['_WORKFLOWPARAMETER_CONSTRAINT']._serialized_end=1265
  _globals['_WORKFLOWPARAMETER_CONSTRAINT_RELATIONTYPE']._serialized_start=1179
  _globals['_WORKFLOWPARAMETER_CONSTRAINT_RELATIONTYPE']._serialized_end=1265
  _globals['_WORKFLOW']._serialized_start=1311
  _globals['_WORKFLOW']._serialized_end=1406
  _globals['_AVAILABLEWORKFLOWS']._serialized_start=1408
  _globals['_AVAILABLEWORKFLOWS']._serialized_end=1458
  _globals['_REQUESTAVAILABLEWORKFLOWS']._serialized_start=1460
  _globals['_REQUESTAVAILABLEWORKFLOWS']._serialized_end=1487
# @@protoc_insertion_point(module_scope)
