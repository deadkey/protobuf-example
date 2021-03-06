# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tof.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tof.proto',
  package='kp',
  syntax='proto3',
  serialized_pb=_b('\n\ttof.proto\x12\x02kp\"a\n\x06Sensor\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06int_ex\x18\x02 \x01(\x03\x12\x10\n\x08\x66loat_ex\x18\x03 \x01(\x02\x12\x13\n\x0b\x64ouble_time\x18\x04 \x01(\x01\x12\x14\n\x0c\x64ouble_value\x18\x05 \x01(\x01\"\"\n\x03ToF\x12\x1b\n\x07sensors\x18\x01 \x03(\x0b\x32\n.kp.Sensorb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SENSOR = _descriptor.Descriptor(
  name='Sensor',
  full_name='kp.Sensor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='kp.Sensor.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='int_ex', full_name='kp.Sensor.int_ex', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='float_ex', full_name='kp.Sensor.float_ex', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='double_time', full_name='kp.Sensor.double_time', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='double_value', full_name='kp.Sensor.double_value', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=114,
)


_TOF = _descriptor.Descriptor(
  name='ToF',
  full_name='kp.ToF',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sensors', full_name='kp.ToF.sensors', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=150,
)

_TOF.fields_by_name['sensors'].message_type = _SENSOR
DESCRIPTOR.message_types_by_name['Sensor'] = _SENSOR
DESCRIPTOR.message_types_by_name['ToF'] = _TOF

Sensor = _reflection.GeneratedProtocolMessageType('Sensor', (_message.Message,), dict(
  DESCRIPTOR = _SENSOR,
  __module__ = 'tof_pb2'
  # @@protoc_insertion_point(class_scope:kp.Sensor)
  ))
_sym_db.RegisterMessage(Sensor)

ToF = _reflection.GeneratedProtocolMessageType('ToF', (_message.Message,), dict(
  DESCRIPTOR = _TOF,
  __module__ = 'tof_pb2'
  # @@protoc_insertion_point(class_scope:kp.ToF)
  ))
_sym_db.RegisterMessage(ToF)


# @@protoc_insertion_point(module_scope)
