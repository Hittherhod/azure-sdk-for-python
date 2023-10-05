# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from marshmallow import ValidationError, fields, validates_schema

from azure.ai.ml._schema.core.schema import PathAwareSchema


class ServerlessComputeSettingsSchema(PathAwareSchema):
    serverless_compute_custom_subnet = fields.Str()
    serverless_compute_no_public_ip = fields.Bool(load_default=False)

    @validates_schema
    def validate_no_public_ip_flag(self, data):
        if data["serverless_compute_no_public_ip"] and len(data["serverless_compute_custom_subnet"]) == 0:
            raise ValidationError(
                "serverless_compute_custom_subnet must be specified if serverless_compute_no_public_ip is set to true"
            )
