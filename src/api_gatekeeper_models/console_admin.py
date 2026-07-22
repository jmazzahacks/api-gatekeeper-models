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
        aegis_user_id: Aegis's pre-contract integer user id. Kept as
            Optional read-only historical data on rows provisioned during
            the phase-1/2 shim. Never populated on new admins after
            phase-3 because Aegis no longer emits it.
    """
    email: str
    created_at: int
    updated_at: int
    aegis_uuid: str
    admin_id: Optional[str] = None
    aegis_user_id: Optional[int] = None

    @classmethod
    def from_dict(cls, data: dict) -> 'ConsoleAdmin':
        """Create a ConsoleAdmin from a database row."""
        return cls(
            admin_id=data['admin_id'],
            aegis_user_id=data.get('aegis_user_id'),
            aegis_uuid=str(data['aegis_uuid']),
            email=data['email'],
            created_at=data['created_at'],
            updated_at=data['updated_at'],
        )

    def to_dict(self) -> dict:
        """Convert to a dictionary for storage or serialization."""
        return {
            'admin_id': self.admin_id,
            'aegis_user_id': self.aegis_user_id,
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
        """Create a new ConsoleAdmin with current timestamp.

        aegis_user_id is intentionally NOT a parameter here — it's read-only
        historical data on shim-era rows loaded via from_dict, and never
        populated on freshly provisioned admins after Aegis phase-3.
        """
        now = int(time.time())
        return cls(
            email=email,
            created_at=now,
            updated_at=now,
            aegis_uuid=aegis_uuid,
            admin_id=admin_id,
        )
