# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/monitoring_v3/proto/alert_service.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.monitoring_v3.proto import (
    alert_pb2 as google_dot_cloud_dot_monitoring__v3_dot_proto_dot_alert__pb2,
)
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/monitoring_v3/proto/alert_service.proto",
    package="google.monitoring.v3",
    syntax="proto3",
    serialized_options=_b(
        "\n\030com.google.monitoring.v3B\021AlertServiceProtoP\001Z>google.golang.org/genproto/googleapis/monitoring/v3;monitoring\252\002\032Google.Cloud.Monitoring.V3\312\002\032Google\\Cloud\\Monitoring\\V3\352\002\035Google::Cloud::Monitoring::V3"
    ),
    serialized_pb=_b(
        '\n4google/cloud/monitoring_v3/proto/alert_service.proto\x12\x14google.monitoring.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a,google/cloud/monitoring_v3/proto/alert.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\x95\x01\n\x18\x43reateAlertPolicyRequest\x12;\n\x04name\x18\x03 \x01(\tB-\xe0\x41\x02\xfa\x41\'\x12%monitoring.googleapis.com/AlertPolicy\x12<\n\x0c\x61lert_policy\x18\x02 \x01(\x0b\x32!.google.monitoring.v3.AlertPolicyB\x03\xe0\x41\x02"T\n\x15GetAlertPolicyRequest\x12;\n\x04name\x18\x03 \x01(\tB-\xe0\x41\x02\xfa\x41\'\n%monitoring.googleapis.com/AlertPolicy"\xa0\x01\n\x18ListAlertPoliciesRequest\x12;\n\x04name\x18\x04 \x01(\tB-\xe0\x41\x02\xfa\x41\'\x12%monitoring.googleapis.com/AlertPolicy\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12\x10\n\x08order_by\x18\x06 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"o\n\x19ListAlertPoliciesResponse\x12\x39\n\x0e\x61lert_policies\x18\x03 \x03(\x0b\x32!.google.monitoring.v3.AlertPolicy\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x89\x01\n\x18UpdateAlertPolicyRequest\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12<\n\x0c\x61lert_policy\x18\x03 \x01(\x0b\x32!.google.monitoring.v3.AlertPolicyB\x03\xe0\x41\x02"W\n\x18\x44\x65leteAlertPolicyRequest\x12;\n\x04name\x18\x03 \x01(\tB-\xe0\x41\x02\xfa\x41\'\n%monitoring.googleapis.com/AlertPolicy2\x9e\x08\n\x12\x41lertPolicyService\x12\xa8\x01\n\x11ListAlertPolicies\x12..google.monitoring.v3.ListAlertPoliciesRequest\x1a/.google.monitoring.v3.ListAlertPoliciesResponse"2\x82\xd3\xe4\x93\x02%\x12#/v3/{name=projects/*}/alertPolicies\xda\x41\x04name\x12\x96\x01\n\x0eGetAlertPolicy\x12+.google.monitoring.v3.GetAlertPolicyRequest\x1a!.google.monitoring.v3.AlertPolicy"4\x82\xd3\xe4\x93\x02\'\x12%/v3/{name=projects/*/alertPolicies/*}\xda\x41\x04name\x12\xb5\x01\n\x11\x43reateAlertPolicy\x12..google.monitoring.v3.CreateAlertPolicyRequest\x1a!.google.monitoring.v3.AlertPolicy"M\x82\xd3\xe4\x93\x02\x33"#/v3/{name=projects/*}/alertPolicies:\x0c\x61lert_policy\xda\x41\x11name,alert_policy\x12\x91\x01\n\x11\x44\x65leteAlertPolicy\x12..google.monitoring.v3.DeleteAlertPolicyRequest\x1a\x16.google.protobuf.Empty"4\x82\xd3\xe4\x93\x02\'*%/v3/{name=projects/*/alertPolicies/*}\xda\x41\x04name\x12\xcb\x01\n\x11UpdateAlertPolicy\x12..google.monitoring.v3.UpdateAlertPolicyRequest\x1a!.google.monitoring.v3.AlertPolicy"c\x82\xd3\xe4\x93\x02\x42\x32\x32/v3/{alert_policy.name=projects/*/alertPolicies/*}:\x0c\x61lert_policy\xda\x41\x18update_mask,alert_policy\x1a\xa9\x01\xca\x41\x19monitoring.googleapis.com\xd2\x41\x89\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/monitoring,https://www.googleapis.com/auth/monitoring.readB\xc9\x01\n\x18\x63om.google.monitoring.v3B\x11\x41lertServiceProtoP\x01Z>google.golang.org/genproto/googleapis/monitoring/v3;monitoring\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3b\x06proto3'
    ),
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_api_dot_client__pb2.DESCRIPTOR,
        google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,
        google_dot_api_dot_resource__pb2.DESCRIPTOR,
        google_dot_cloud_dot_monitoring__v3_dot_proto_dot_alert__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,
    ],
)


_CREATEALERTPOLICYREQUEST = _descriptor.Descriptor(
    name="CreateAlertPolicyRequest",
    full_name="google.monitoring.v3.CreateAlertPolicyRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.monitoring.v3.CreateAlertPolicyRequest.name",
            index=0,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b(
                "\340A\002\372A'\022%monitoring.googleapis.com/AlertPolicy"
            ),
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="alert_policy",
            full_name="google.monitoring.v3.CreateAlertPolicyRequest.alert_policy",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b("\340A\002"),
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=303,
    serialized_end=452,
)


_GETALERTPOLICYREQUEST = _descriptor.Descriptor(
    name="GetAlertPolicyRequest",
    full_name="google.monitoring.v3.GetAlertPolicyRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.monitoring.v3.GetAlertPolicyRequest.name",
            index=0,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b(
                "\340A\002\372A'\n%monitoring.googleapis.com/AlertPolicy"
            ),
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=454,
    serialized_end=538,
)


_LISTALERTPOLICIESREQUEST = _descriptor.Descriptor(
    name="ListAlertPoliciesRequest",
    full_name="google.monitoring.v3.ListAlertPoliciesRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.monitoring.v3.ListAlertPoliciesRequest.name",
            index=0,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b(
                "\340A\002\372A'\022%monitoring.googleapis.com/AlertPolicy"
            ),
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="filter",
            full_name="google.monitoring.v3.ListAlertPoliciesRequest.filter",
            index=1,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="order_by",
            full_name="google.monitoring.v3.ListAlertPoliciesRequest.order_by",
            index=2,
            number=6,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="page_size",
            full_name="google.monitoring.v3.ListAlertPoliciesRequest.page_size",
            index=3,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="page_token",
            full_name="google.monitoring.v3.ListAlertPoliciesRequest.page_token",
            index=4,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=541,
    serialized_end=701,
)


_LISTALERTPOLICIESRESPONSE = _descriptor.Descriptor(
    name="ListAlertPoliciesResponse",
    full_name="google.monitoring.v3.ListAlertPoliciesResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="alert_policies",
            full_name="google.monitoring.v3.ListAlertPoliciesResponse.alert_policies",
            index=0,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="next_page_token",
            full_name="google.monitoring.v3.ListAlertPoliciesResponse.next_page_token",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=703,
    serialized_end=814,
)


_UPDATEALERTPOLICYREQUEST = _descriptor.Descriptor(
    name="UpdateAlertPolicyRequest",
    full_name="google.monitoring.v3.UpdateAlertPolicyRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="update_mask",
            full_name="google.monitoring.v3.UpdateAlertPolicyRequest.update_mask",
            index=0,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="alert_policy",
            full_name="google.monitoring.v3.UpdateAlertPolicyRequest.alert_policy",
            index=1,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b("\340A\002"),
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=817,
    serialized_end=954,
)


_DELETEALERTPOLICYREQUEST = _descriptor.Descriptor(
    name="DeleteAlertPolicyRequest",
    full_name="google.monitoring.v3.DeleteAlertPolicyRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.monitoring.v3.DeleteAlertPolicyRequest.name",
            index=0,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b(
                "\340A\002\372A'\n%monitoring.googleapis.com/AlertPolicy"
            ),
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=956,
    serialized_end=1043,
)

_CREATEALERTPOLICYREQUEST.fields_by_name[
    "alert_policy"
].message_type = (
    google_dot_cloud_dot_monitoring__v3_dot_proto_dot_alert__pb2._ALERTPOLICY
)
_LISTALERTPOLICIESRESPONSE.fields_by_name[
    "alert_policies"
].message_type = (
    google_dot_cloud_dot_monitoring__v3_dot_proto_dot_alert__pb2._ALERTPOLICY
)
_UPDATEALERTPOLICYREQUEST.fields_by_name[
    "update_mask"
].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_UPDATEALERTPOLICYREQUEST.fields_by_name[
    "alert_policy"
].message_type = (
    google_dot_cloud_dot_monitoring__v3_dot_proto_dot_alert__pb2._ALERTPOLICY
)
DESCRIPTOR.message_types_by_name["CreateAlertPolicyRequest"] = _CREATEALERTPOLICYREQUEST
DESCRIPTOR.message_types_by_name["GetAlertPolicyRequest"] = _GETALERTPOLICYREQUEST
DESCRIPTOR.message_types_by_name["ListAlertPoliciesRequest"] = _LISTALERTPOLICIESREQUEST
DESCRIPTOR.message_types_by_name[
    "ListAlertPoliciesResponse"
] = _LISTALERTPOLICIESRESPONSE
DESCRIPTOR.message_types_by_name["UpdateAlertPolicyRequest"] = _UPDATEALERTPOLICYREQUEST
DESCRIPTOR.message_types_by_name["DeleteAlertPolicyRequest"] = _DELETEALERTPOLICYREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateAlertPolicyRequest = _reflection.GeneratedProtocolMessageType(
    "CreateAlertPolicyRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_CREATEALERTPOLICYREQUEST,
        __module__="google.cloud.monitoring_v3.proto.alert_service_pb2",
        __doc__="""The protocol for the ``CreateAlertPolicy`` request.
  Attributes:
      name:
          Required. The project in which to create the alerting policy.
          The format is:  ::      projects/[PROJECT_ID_OR_NUMBER]  Note
          that this field names the parent container in which the
          alerting policy will be written, not the name of the created
          policy. The alerting policy that is returned will have a name
          that contains a normalized representation of this name as a
          prefix but adds a suffix of the form
          ``/alertPolicies/[ALERT_POLICY_ID]``, identifying the policy
          in the container.
      alert_policy:
          Required. The requested alerting policy. You should omit the
          ``name`` field in this policy. The name will be returned in
          the new policy, including a new ``[ALERT_POLICY_ID]`` value.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.v3.CreateAlertPolicyRequest)
    ),
)
_sym_db.RegisterMessage(CreateAlertPolicyRequest)

GetAlertPolicyRequest = _reflection.GeneratedProtocolMessageType(
    "GetAlertPolicyRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_GETALERTPOLICYREQUEST,
        __module__="google.cloud.monitoring_v3.proto.alert_service_pb2",
        __doc__="""The protocol for the ``GetAlertPolicy`` request.
  Attributes:
      name:
          Required. The alerting policy to retrieve. The format is:  ::
          projects/[PROJECT_ID_OR_NUMBER]/alertPolicies/[ALERT_POLICY_ID
          ]
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.v3.GetAlertPolicyRequest)
    ),
)
_sym_db.RegisterMessage(GetAlertPolicyRequest)

ListAlertPoliciesRequest = _reflection.GeneratedProtocolMessageType(
    "ListAlertPoliciesRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_LISTALERTPOLICIESREQUEST,
        __module__="google.cloud.monitoring_v3.proto.alert_service_pb2",
        __doc__="""The protocol for the ``ListAlertPolicies`` request.
  Attributes:
      name:
          Required. The project whose alert policies are to be listed.
          The format is:  ::      projects/[PROJECT_ID_OR_NUMBER]  Note
          that this field names the parent container in which the
          alerting policies to be listed are stored. To retrieve a
          single alerting policy by name, use the [GetAlertPolicy][googl
          e.monitoring.v3.AlertPolicyService.GetAlertPolicy] operation,
          instead.
      filter:
          If provided, this field specifies the criteria that must be
          met by alert policies to be included in the response.  For
          more details, see `sorting and filtering
          <https://cloud.google.com/monitoring/api/v3/sorting-and-
          filtering>`__.
      order_by:
          A comma-separated list of fields by which to sort the result.
          Supports the same set of field references as the ``filter``
          field. Entries can be prefixed with a minus sign to sort by
          the field in descending order.  For more details, see `sorting
          and filtering
          <https://cloud.google.com/monitoring/api/v3/sorting-and-
          filtering>`__.
      page_size:
          The maximum number of results to return in a single response.
      page_token:
          If this field is not empty then it must contain the
          ``nextPageToken`` value returned by a previous call to this
          method. Using this field causes the method to return more
          results from the previous method call.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.v3.ListAlertPoliciesRequest)
    ),
)
_sym_db.RegisterMessage(ListAlertPoliciesRequest)

ListAlertPoliciesResponse = _reflection.GeneratedProtocolMessageType(
    "ListAlertPoliciesResponse",
    (_message.Message,),
    dict(
        DESCRIPTOR=_LISTALERTPOLICIESRESPONSE,
        __module__="google.cloud.monitoring_v3.proto.alert_service_pb2",
        __doc__="""The protocol for the ``ListAlertPolicies`` response.
  Attributes:
      alert_policies:
          The returned alert policies.
      next_page_token:
          If there might be more results than were returned, then this
          field is set to a non-empty value. To see the additional
          results, use that value as ``page_token`` in the next call to
          this method.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.v3.ListAlertPoliciesResponse)
    ),
)
_sym_db.RegisterMessage(ListAlertPoliciesResponse)

UpdateAlertPolicyRequest = _reflection.GeneratedProtocolMessageType(
    "UpdateAlertPolicyRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_UPDATEALERTPOLICYREQUEST,
        __module__="google.cloud.monitoring_v3.proto.alert_service_pb2",
        __doc__="""The protocol for the ``UpdateAlertPolicy`` request.
  Attributes:
      update_mask:
          Optional. A list of alerting policy field names. If this field
          is not empty, each listed field in the existing alerting
          policy is set to the value of the corresponding field in the
          supplied policy (``alert_policy``), or to the field's default
          value if the field is not in the supplied alerting policy.
          Fields not listed retain their previous value.  Examples of
          valid field masks include ``display_name``, ``documentation``,
          ``documentation.content``, ``documentation.mime_type``,
          ``user_labels``, ``user_label.nameofkey``, ``enabled``,
          ``conditions``, ``combiner``, etc.  If this field is empty,
          then the supplied alerting policy replaces the existing
          policy. It is the same as deleting the existing policy and
          adding the supplied policy, except for the following:  -  The
          new policy will have the same ``[ALERT_POLICY_ID]`` as the
          former    policy. This gives you continuity with the former
          policy in your    notifications and incidents. -  Conditions
          in the new policy will keep their former    ``[CONDITION_ID]``
          if the supplied condition includes the ``name``    field with
          that ``[CONDITION_ID]``. If the supplied condition omits
          the ``name`` field, then a new ``[CONDITION_ID]`` is created.
      alert_policy:
          Required. The updated alerting policy or the updated values
          for the fields listed in ``update_mask``. If ``update_mask``
          is not empty, any fields in this policy that are not in
          ``update_mask`` are ignored.
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.v3.UpdateAlertPolicyRequest)
    ),
)
_sym_db.RegisterMessage(UpdateAlertPolicyRequest)

DeleteAlertPolicyRequest = _reflection.GeneratedProtocolMessageType(
    "DeleteAlertPolicyRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_DELETEALERTPOLICYREQUEST,
        __module__="google.cloud.monitoring_v3.proto.alert_service_pb2",
        __doc__="""The protocol for the ``DeleteAlertPolicy`` request.
  Attributes:
      name:
          Required. The alerting policy to delete. The format is:  ::
          projects/[PROJECT_ID_OR_NUMBER]/alertPolicies/[ALERT_POLICY_ID
          ]  For more information, see
          [AlertPolicy][google.monitoring.v3.AlertPolicy].
  """,
        # @@protoc_insertion_point(class_scope:google.monitoring.v3.DeleteAlertPolicyRequest)
    ),
)
_sym_db.RegisterMessage(DeleteAlertPolicyRequest)


DESCRIPTOR._options = None
_CREATEALERTPOLICYREQUEST.fields_by_name["name"]._options = None
_CREATEALERTPOLICYREQUEST.fields_by_name["alert_policy"]._options = None
_GETALERTPOLICYREQUEST.fields_by_name["name"]._options = None
_LISTALERTPOLICIESREQUEST.fields_by_name["name"]._options = None
_UPDATEALERTPOLICYREQUEST.fields_by_name["alert_policy"]._options = None
_DELETEALERTPOLICYREQUEST.fields_by_name["name"]._options = None

_ALERTPOLICYSERVICE = _descriptor.ServiceDescriptor(
    name="AlertPolicyService",
    full_name="google.monitoring.v3.AlertPolicyService",
    file=DESCRIPTOR,
    index=0,
    serialized_options=_b(
        "\312A\031monitoring.googleapis.com\322A\211\001https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/monitoring,https://www.googleapis.com/auth/monitoring.read"
    ),
    serialized_start=1046,
    serialized_end=2100,
    methods=[
        _descriptor.MethodDescriptor(
            name="ListAlertPolicies",
            full_name="google.monitoring.v3.AlertPolicyService.ListAlertPolicies",
            index=0,
            containing_service=None,
            input_type=_LISTALERTPOLICIESREQUEST,
            output_type=_LISTALERTPOLICIESRESPONSE,
            serialized_options=_b(
                "\202\323\344\223\002%\022#/v3/{name=projects/*}/alertPolicies\332A\004name"
            ),
        ),
        _descriptor.MethodDescriptor(
            name="GetAlertPolicy",
            full_name="google.monitoring.v3.AlertPolicyService.GetAlertPolicy",
            index=1,
            containing_service=None,
            input_type=_GETALERTPOLICYREQUEST,
            output_type=google_dot_cloud_dot_monitoring__v3_dot_proto_dot_alert__pb2._ALERTPOLICY,
            serialized_options=_b(
                "\202\323\344\223\002'\022%/v3/{name=projects/*/alertPolicies/*}\332A\004name"
            ),
        ),
        _descriptor.MethodDescriptor(
            name="CreateAlertPolicy",
            full_name="google.monitoring.v3.AlertPolicyService.CreateAlertPolicy",
            index=2,
            containing_service=None,
            input_type=_CREATEALERTPOLICYREQUEST,
            output_type=google_dot_cloud_dot_monitoring__v3_dot_proto_dot_alert__pb2._ALERTPOLICY,
            serialized_options=_b(
                '\202\323\344\223\0023"#/v3/{name=projects/*}/alertPolicies:\014alert_policy\332A\021name,alert_policy'
            ),
        ),
        _descriptor.MethodDescriptor(
            name="DeleteAlertPolicy",
            full_name="google.monitoring.v3.AlertPolicyService.DeleteAlertPolicy",
            index=3,
            containing_service=None,
            input_type=_DELETEALERTPOLICYREQUEST,
            output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
            serialized_options=_b(
                "\202\323\344\223\002'*%/v3/{name=projects/*/alertPolicies/*}\332A\004name"
            ),
        ),
        _descriptor.MethodDescriptor(
            name="UpdateAlertPolicy",
            full_name="google.monitoring.v3.AlertPolicyService.UpdateAlertPolicy",
            index=4,
            containing_service=None,
            input_type=_UPDATEALERTPOLICYREQUEST,
            output_type=google_dot_cloud_dot_monitoring__v3_dot_proto_dot_alert__pb2._ALERTPOLICY,
            serialized_options=_b(
                "\202\323\344\223\002B22/v3/{alert_policy.name=projects/*/alertPolicies/*}:\014alert_policy\332A\030update_mask,alert_policy"
            ),
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_ALERTPOLICYSERVICE)

DESCRIPTOR.services_by_name["AlertPolicyService"] = _ALERTPOLICYSERVICE

# @@protoc_insertion_point(module_scope)
