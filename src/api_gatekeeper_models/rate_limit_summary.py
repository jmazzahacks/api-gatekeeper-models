"""
RateLimitSummary: wire-format projection of a RateLimit joined with the
client_name from its Client. Produced by the admin endpoint and consumed by
the console frontend.
"""
from dataclasses import dataclass

from .client import Client
from .rate_limit import RateLimit


@dataclass
class RateLimitSummary:
    """A RateLimit joined with the client_name for the console table."""
    client_id: str
    client_name: str
    requests_per_day: int
    created_at: int
    updated_at: int

    @classmethod
    def from_join(cls, rate_limit: RateLimit, client: Client) -> 'RateLimitSummary':
        if client.client_id is None:
            raise ValueError("Cannot summarize against an unsaved Client")
        if rate_limit.client_id != client.client_id:
            raise ValueError("rate_limit.client_id does not match client.client_id")
        return cls(
            client_id=rate_limit.client_id,
            client_name=client.client_name,
            requests_per_day=rate_limit.requests_per_day,
            created_at=rate_limit.created_at,
            updated_at=rate_limit.updated_at,
        )

    @classmethod
    def from_dict(cls, data: dict) -> 'RateLimitSummary':
        return cls(
            client_id=str(data['client_id']),
            client_name=str(data['client_name']),
            requests_per_day=int(data['requests_per_day']),
            created_at=int(data['created_at']),
            updated_at=int(data['updated_at']),
        )

    def to_dict(self) -> dict:
        return {
            'client_id': self.client_id,
            'client_name': self.client_name,
            'requests_per_day': self.requests_per_day,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
