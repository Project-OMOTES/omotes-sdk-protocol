"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Parameter(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _ParameterType:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ParameterTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Parameter._ParameterType.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        STRING: Parameter._ParameterType.ValueType  # 0
        INTEGER: Parameter._ParameterType.ValueType  # 1
        DOUBLE: Parameter._ParameterType.ValueType  # 2
        DATETIME: Parameter._ParameterType.ValueType  # 3

    class ParameterType(_ParameterType, metaclass=_ParameterTypeEnumTypeWrapper): ...
    STRING: Parameter.ParameterType.ValueType  # 0
    INTEGER: Parameter.ParameterType.ValueType  # 1
    DOUBLE: Parameter.ParameterType.ValueType  # 2
    DATETIME: Parameter.ParameterType.ValueType  # 3

    NAME_FIELD_NUMBER: builtins.int
    PARAMETER_TYPE_FIELD_NUMBER: builtins.int
    name: builtins.str
    parameter_type: global___Parameter.ParameterType.ValueType
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        parameter_type: global___Parameter.ParameterType.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name", "parameter_type", b"parameter_type"]) -> None: ...

global___Parameter = Parameter

@typing_extensions.final
class WorkFlow(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TYPE_NAME_FIELD_NUMBER: builtins.int
    TYPE_DESCRIPTION_FIELD_NUMBER: builtins.int
    ADDITIONAL_PARAMETERS_FIELD_NUMBER: builtins.int
    type_name: builtins.str
    type_description: builtins.str
    @property
    def additional_parameters(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Parameter]: ...
    def __init__(
        self,
        *,
        type_name: builtins.str = ...,
        type_description: builtins.str = ...,
        additional_parameters: collections.abc.Iterable[global___Parameter] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["additional_parameters", b"additional_parameters", "type_description", b"type_description", "type_name", b"type_name"]) -> None: ...

global___WorkFlow = WorkFlow

@typing_extensions.final
class AvailableWorkFlows(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WORK_FLOWS_FIELD_NUMBER: builtins.int
    @property
    def work_flows(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___WorkFlow]: ...
    def __init__(
        self,
        *,
        work_flows: collections.abc.Iterable[global___WorkFlow] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["work_flows", b"work_flows"]) -> None: ...

global___AvailableWorkFlows = AvailableWorkFlows

@typing_extensions.final
class RequestAvailableWorkflows(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___RequestAvailableWorkflows = RequestAvailableWorkflows