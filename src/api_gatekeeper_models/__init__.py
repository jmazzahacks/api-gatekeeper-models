"""
Shared data models for the API Gatekeeper auth service.
"""

__version__ = "0.2.0"

from .route import Route, HttpMethod
from .method_auth import MethodAuth, AuthType
from .client import Client, ClientStatus
from .client_permission import ClientPermission
from .client_summary import ClientSummary
from .permission_summary import PermissionSummary
from .rate_limit import RateLimit
from .console_admin import ConsoleAdmin

__all__ = [
    'Route',
    'HttpMethod',
    'MethodAuth',
    'AuthType',
    'Client',
    'ClientStatus',
    'ClientPermission',
    'ClientSummary',
    'PermissionSummary',
    'RateLimit',
    'ConsoleAdmin',
]
