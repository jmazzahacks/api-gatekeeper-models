"""
ClientSummary: redacted wire-format projection of Client for admin listings.

Produced by the docker-backend admin endpoint and consumed by the console
frontend. Never carries shared_secret. api_key is masked.
"""
from dataclasses import dataclass

from .client import Client, ClientStatus


_MASK_PREFIX = 8
_MASK_SUFFIX = 4


def _mask_api_key(api_key: str) -> str:
    if len(api_key) <= _MASK_PREFIX + _MASK_SUFFIX:
        return '*' * len(api_key)
    return f'{api_key[:_MASK_PREFIX]}…{api_key[-_MASK_SUFFIX:]}'


@dataclass
class ClientSummary:
    """Redacted projection of a Client for the admin console list view."""
    client_id: str
    client_name: str
    status: ClientStatus
    api_key_masked: str
    created_at: int
    updated_at: int

    @classmethod
    def from_client(cls, client: Client) -> 'ClientSummary':
        if client.client_id is None:
            raise ValueError("Cannot summarize an unsaved Client (client_id is None)")
        return cls(
            client_id=client.client_id,
            client_name=client.client_name,
            status=client.status,
            api_key_masked=_mask_api_key(client.api_key or ''),
            created_at=client.created_at,
            updated_at=client.updated_at,
        )

    def to_dict(self) -> dict:
        return {
            'client_id': self.client_id,
            'client_name': self.client_name,
            'status': self.status.value,
            'api_key_masked': self.api_key_masked,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
