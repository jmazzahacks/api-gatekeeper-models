"""
Shared data models for the API Gatekeeper auth service.
"""

__version__ = "0.1.0"

from .route import Route, HttpMethod
from .method_auth import MethodAuth, AuthType
from .client import Client, ClientStatus
from .client_permission import ClientPermission
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
    'RateLimit',
    'ConsoleAdmin',
]
