# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: work_flow.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fwork_flow.proto\"\x8f\x01\n\tParameter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x30\n\x0eparameter_type\x18\x02 \x01(\x0e\x32\x18.Parameter.ParameterType\"B\n\rParameterType\x12\n\n\x06STRING\x10\x00\x12\x0b\n\x07INTEGER\x10\x01\x12\n\n\x06\x44OUBLE\x10\x02\x12\x0c\n\x08\x44\x41TETIME\x10\x03\"b\n\x08WorkFlow\x12\x11\n\ttype_name\x18\x01 \x01(\t\x12\x18\n\x10type_description\x18\x02 \x01(\t\x12)\n\x15\x61\x64\x64itional_parameters\x18\x03 \x03(\x0b\x32\n.Parameter\"3\n\x12\x41vailableWorkFlows\x12\x1d\n\nwork_flows\x18\x01 \x03(\x0b\x32\t.WorkFlow\"\x1b\n\x19RequestAvailableWorkflowsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'work_flow_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_PARAMETER']._serialized_start=20
  _globals['_PARAMETER']._serialized_end=163
  _globals['_PARAMETER_PARAMETERTYPE']._serialized_start=97
  _globals['_PARAMETER_PARAMETERTYPE']._serialized_end=163
  _globals['_WORKFLOW']._serialized_start=165
  _globals['_WORKFLOW']._serialized_end=263
  _globals['_AVAILABLEWORKFLOWS']._serialized_start=265
  _globals['_AVAILABLEWORKFLOWS']._serialized_end=316
  _globals['_REQUESTAVAILABLEWORKFLOWS']._serialized_start=318
  _globals['_REQUESTAVAILABLEWORKFLOWS']._serialized_end=345
# @@protoc_insertion_point(module_scope)