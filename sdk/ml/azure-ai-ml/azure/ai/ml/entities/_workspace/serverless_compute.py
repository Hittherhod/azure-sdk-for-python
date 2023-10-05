# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
from typing import Optional

from azure.ai.ml._restclient.v2023_08_01_preview.models import (
    ServerlessComputeSettings as RestServerlessComputeSettings,
)


class ServerlessComputeSettings:
    """Settings regarding serverless compute(s) in an Azure ML workspace.

    :param serverless_compute_custom_subnet: The name of the subnet to use for serverless compute(s).
    :type serverless_compute_custom_subnet: Optional[str]
    :param serverless_compute_no_public_ip: Whether or not to disable public IP addresses for serverless compute(s).
    :type serverless_compute_no_public_ip: bool
    """

    serverless_compute_custom_subnet: Optional[str]
    serverless_compute_no_public_ip: bool = False

    def __init__(
        self, serverless_compute_custom_subnet: Optional[str] = None, serverless_compute_no_public_ip: bool = False
    ):
        if (
            serverless_compute_custom_subnet is None or len(serverless_compute_custom_subnet) == 0
        ) and serverless_compute_no_public_ip:
            raise ValueError(
                "serverless_compute_custom_subnet must be specified if serverless_compute_no_public_ip is set to true"
            )
        self.serverless_compute_custom_subnet = serverless_compute_custom_subnet
        self.serverless_compute_no_public_ip = serverless_compute_no_public_ip

    def __eq__(self, other: "ServerlessComputeSettings") -> bool:
        if not isinstance(other, ServerlessComputeSettings):
            return False
        return (
            self.serverless_compute_custom_subnet == other.serverless_compute_custom_subnet
            and self.serverless_compute_no_public_ip == other.serverless_compute_no_public_ip
        )

    def _to_rest_object(self) -> RestServerlessComputeSettings:
        return RestServerlessComputeSettings(
            serverless_compute_custom_subnet=self.serverless_compute_custom_subnet,
            serverless_compute_no_public_ip=self.serverless_compute_no_public_ip,
        )

    @classmethod
    def _from_rest_object(cls, obj: RestServerlessComputeSettings) -> "ServerlessComputeSettings":
        return ServerlessComputeSettings(
            serverless_compute_custom_subnet=obj.serverless_compute_custom_subnet,
            serverless_compute_no_public_ip=obj.serverless_compute_no_public_ip,
        )
