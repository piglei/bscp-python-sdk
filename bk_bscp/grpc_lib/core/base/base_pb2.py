# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pkg/protocol/core/base/base.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!pkg/protocol/core/base/base.proto\x12\x06pbbase\"R\n\x08Revision\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\x0f\n\x07reviser\x18\x02 \x01(\t\x12\x11\n\tcreate_at\x18\x03 \x01(\t\x12\x11\n\tupdate_at\x18\x04 \x01(\t\"5\n\x0f\x43reatedRevision\x12\x0f\n\x07\x63reator\x18\x01 \x01(\t\x12\x11\n\tcreate_at\x18\x02 \x01(\t\"T\n\x08\x42\x61sePage\x12\r\n\x05\x63ount\x18\x01 \x01(\x08\x12\r\n\x05start\x18\x02 \x01(\r\x12\r\n\x05limit\x18\x03 \x01(\r\x12\x0c\n\x04sort\x18\x04 \x01(\t\x12\r\n\x05order\x18\x05 \x01(\t\"\n\n\x08\x45mptyReq\"\x0b\n\tEmptyResp\")\n\x08\x42\x61seResp\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"9\n\nVersioning\x12\r\n\x05Major\x18\x01 \x01(\r\x12\r\n\x05Minor\x18\x02 \x01(\r\x12\r\n\x05Patch\x18\x03 \x01(\r\"1\n\x0fInvalidArgument\x12\r\n\x05\x66ield\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\tBWZUgithub.com/TencentBlueKing/bk-bcs/bcs-services/bcs-bscp/pkg/protocol/core/base;pbbaseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pkg.protocol.core.base.base_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZUgithub.com/TencentBlueKing/bk-bcs/bcs-services/bcs-bscp/pkg/protocol/core/base;pbbase'
  _globals['_REVISION']._serialized_start=45
  _globals['_REVISION']._serialized_end=127
  _globals['_CREATEDREVISION']._serialized_start=129
  _globals['_CREATEDREVISION']._serialized_end=182
  _globals['_BASEPAGE']._serialized_start=184
  _globals['_BASEPAGE']._serialized_end=268
  _globals['_EMPTYREQ']._serialized_start=270
  _globals['_EMPTYREQ']._serialized_end=280
  _globals['_EMPTYRESP']._serialized_start=282
  _globals['_EMPTYRESP']._serialized_end=293
  _globals['_BASERESP']._serialized_start=295
  _globals['_BASERESP']._serialized_end=336
  _globals['_VERSIONING']._serialized_start=338
  _globals['_VERSIONING']._serialized_end=395
  _globals['_INVALIDARGUMENT']._serialized_start=397
  _globals['_INVALIDARGUMENT']._serialized_end=446
# @@protoc_insertion_point(module_scope)