# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: animalai/communicator_objects/unity_output.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from animalai.communicator_objects import unity_rl_output_pb2 as animalai_dot_communicator__objects_dot_unity__rl__output__pb2
from animalai.communicator_objects import unity_rl_initialization_output_pb2 as animalai_dot_communicator__objects_dot_unity__rl__initialization__output__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='animalai/communicator_objects/unity_output.proto',
  package='communicator_objects',
  syntax='proto3',
  serialized_options=_b('\252\002\034MLAgents.CommunicatorObjects'),
  serialized_pb=_b('\n0animalai/communicator_objects/unity_output.proto\x12\x14\x63ommunicator_objects\x1a\x33\x61nimalai/communicator_objects/unity_rl_output.proto\x1a\x42\x61nimalai/communicator_objects/unity_rl_initialization_output.proto\"\x9a\x01\n\x0bUnityOutput\x12\x36\n\trl_output\x18\x01 \x01(\x0b\x32#.communicator_objects.UnityRLOutput\x12S\n\x18rl_initialization_output\x18\x02 \x01(\x0b\x32\x31.communicator_objects.UnityRLInitializationOutputB\x1f\xaa\x02\x1cMLAgents.CommunicatorObjectsb\x06proto3')
  ,
  dependencies=[animalai_dot_communicator__objects_dot_unity__rl__output__pb2.DESCRIPTOR,animalai_dot_communicator__objects_dot_unity__rl__initialization__output__pb2.DESCRIPTOR,])




_UNITYOUTPUT = _descriptor.Descriptor(
  name='UnityOutput',
  full_name='communicator_objects.UnityOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rl_output', full_name='communicator_objects.UnityOutput.rl_output', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rl_initialization_output', full_name='communicator_objects.UnityOutput.rl_initialization_output', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=196,
  serialized_end=350,
)

_UNITYOUTPUT.fields_by_name['rl_output'].message_type = animalai_dot_communicator__objects_dot_unity__rl__output__pb2._UNITYRLOUTPUT
_UNITYOUTPUT.fields_by_name['rl_initialization_output'].message_type = animalai_dot_communicator__objects_dot_unity__rl__initialization__output__pb2._UNITYRLINITIALIZATIONOUTPUT
DESCRIPTOR.message_types_by_name['UnityOutput'] = _UNITYOUTPUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UnityOutput = _reflection.GeneratedProtocolMessageType('UnityOutput', (_message.Message,), {
  'DESCRIPTOR' : _UNITYOUTPUT,
  '__module__' : 'animalai.communicator_objects.unity_output_pb2'
  # @@protoc_insertion_point(class_scope:communicator_objects.UnityOutput)
  })
_sym_db.RegisterMessage(UnityOutput)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
