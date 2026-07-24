"""
ConsoleAdmin model for the Gatekeeper admin console.

A ConsoleAdmin is a human user (linked to an Aegis account) who is authorized
to log in to the management console and administer clients, routes, and
permissions. This is distinct from a `Client`, which represents an API
credential used to authenticate to protected routes.
"""
from typing import Optional
from dataclasses import dataclass
import time


@dataclass
class ConsoleAdmin:
    """
    Represents a console administrator provisioned from an Aegis account.

    Attributes:
        email: The admin's email address (unique)
        created_at: Unix timestamp of when the admin was provisioned
        updated_at: Unix timestamp of last update
        aegis_uuid: The Aegis-side user UUID — source of truth for admin
            identity after Aegis phase-3 (UUID-only contract). New admins
            provisioned via the phase-3 webhook always carry a UUID.
        admin_id: Local unique identifier (auto-generated if None)
    """
    email: str
    created_at: int
    updated_at: int
    aegis_uuid: str
    admin_id: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict) -> 'ConsoleAdmin':
        """Create a ConsoleAdmin from a database row."""
        return cls(
            admin_id=data['admin_id'],
            aegis_uuid=str(data['aegis_uuid']),
            email=data['email'],
            created_at=data['created_at'],
            updated_at=data['updated_at'],
        )

    def to_dict(self) -> dict:
        """Convert to a dictionary for storage or serialization."""
        return {
            'admin_id': self.admin_id,
            'aegis_uuid': self.aegis_uuid,
            'email': self.email,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }

    @classmethod
    def create_new(
        cls,
        email: str,
        aegis_uuid: str,
        admin_id: Optional[str] = None,
    ) -> 'ConsoleAdmin':
        """Create a new ConsoleAdmin with current timestamp."""
        now = int(time.time())
        return cls(
            email=email,
            created_at=now,
            updated_at=now,
            aegis_uuid=aegis_uuid,
            admin_id=admin_id,
        )
