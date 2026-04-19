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
        aegis_user_id: The Aegis-side user ID that identifies this admin
        email: The admin's email address (unique)
        created_at: Unix timestamp of when the admin was provisioned
        updated_at: Unix timestamp of last update
        admin_id: Local unique identifier (auto-generated if None)
    """
    aegis_user_id: int
    email: str
    created_at: int
    updated_at: int
    admin_id: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict) -> 'ConsoleAdmin':
        """Create a ConsoleAdmin from a database row."""
        return cls(
            admin_id=data['admin_id'],
            aegis_user_id=data['aegis_user_id'],
            email=data['email'],
            created_at=data['created_at'],
            updated_at=data['updated_at'],
        )

    def to_dict(self) -> dict:
        """Convert to a dictionary for storage or serialization."""
        return {
            'admin_id': self.admin_id,
            'aegis_user_id': self.aegis_user_id,
            'email': self.email,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }

    @classmethod
    def create_new(
        cls,
        aegis_user_id: int,
        email: str,
        admin_id: Optional[str] = None,
    ) -> 'ConsoleAdmin':
        """Create a new ConsoleAdmin with current timestamp."""
        now = int(time.time())
        return cls(
            aegis_user_id=aegis_user_id,
            email=email,
            created_at=now,
            updated_at=now,
            admin_id=admin_id,
        )
