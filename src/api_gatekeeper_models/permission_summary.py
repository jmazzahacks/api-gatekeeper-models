"""
PermissionSummary: wire-format projection of a ClientPermission joined with
the display fields from its Client and Route. Produced by the admin endpoint
and consumed by the console frontend.
"""
from dataclasses import dataclass
from typing import List

from .client import Client
from .client_permission import ClientPermission
from .route import HttpMethod, Route


@dataclass
class PermissionSummary:
    """A ClientPermission joined with display fields for the console table."""
    permission_id: str
    client_id: str
    client_name: str
    route_id: str
    route_domain: str
    route_pattern: str
    route_service_name: str
    allowed_methods: List[HttpMethod]
    created_at: int

    @classmethod
    def from_join(
        cls,
        permission: ClientPermission,
        client: Client,
        route: Route,
    ) -> 'PermissionSummary':
        if permission.permission_id is None:
            raise ValueError("Cannot summarize an unsaved ClientPermission")
        if client.client_id is None or route.route_id is None:
            raise ValueError("Cannot summarize against unsaved Client/Route")
        return cls(
            permission_id=permission.permission_id,
            client_id=client.client_id,
            client_name=client.client_name,
            route_id=route.route_id,
            route_domain=route.domain,
            route_pattern=route.route_pattern,
            route_service_name=route.service_name,
            allowed_methods=list(permission.allowed_methods),
            created_at=permission.created_at,
        )

    @classmethod
    def from_dict(cls, data: dict) -> 'PermissionSummary':
        """Reconstruct a PermissionSummary from its to_dict() wire format.

        Used by API client libraries (e.g. api-gatekeeper-api-python) to
        deserialize gatekeeper admin responses back into typed models. Raises
        KeyError on missing fields and ValueError on unknown HTTP methods.
        """
        return cls(
            permission_id=str(data['permission_id']),
            client_id=str(data['client_id']),
            client_name=str(data['client_name']),
            route_id=str(data['route_id']),
            route_domain=str(data['route_domain']),
            route_pattern=str(data['route_pattern']),
            route_service_name=str(data['route_service_name']),
            allowed_methods=[HttpMethod(m) for m in data['allowed_methods']],
            created_at=int(data['created_at']),
        )

    def to_dict(self) -> dict:
        return {
            'permission_id': self.permission_id,
            'client_id': self.client_id,
            'client_name': self.client_name,
            'route_id': self.route_id,
            'route_domain': self.route_domain,
            'route_pattern': self.route_pattern,
            'route_service_name': self.route_service_name,
            'allowed_methods': [m.value for m in self.allowed_methods],
            'created_at': self.created_at,
        }
