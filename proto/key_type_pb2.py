# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: key_type.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0ekey_type.proto*/\n\x08Key_Type\x12\x0f\n\x0bWA_PROVIDED\x10\x00\x12\x12\n\x0eHSM_CONTROLLED\x10\x01\x62\x06proto3')

_KEY_TYPE = DESCRIPTOR.enum_types_by_name['Key_Type']
Key_Type = enum_type_wrapper.EnumTypeWrapper(_KEY_TYPE)
WA_PROVIDED = 0
HSM_CONTROLLED = 1


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _KEY_TYPE._serialized_start=18
  _KEY_TYPE._serialized_end=65
# @@protoc_insertion_point(module_scope)