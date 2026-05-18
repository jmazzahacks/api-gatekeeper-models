"""
Shared data models for the API Gatekeeper auth service.
"""
from importlib.metadata import version

# Single source of truth: read from installed package metadata produced by
# hatchling at build time. pyproject.toml [project].version is canonical;
# this just exposes it at runtime for `api_gatekeeper_models.__version__`.
__version__ = version("api-gatekeeper-models")

from .route import Route, HttpMethod
from .method_auth import MethodAuth, AuthType
from .client import Client, ClientStatus
from .client_permission import ClientPermission
from .client_summary import ClientSummary
from .permission_summary import PermissionSummary
from .rate_limit import RateLimit
from .rate_limit_summary import RateLimitSummary
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
    'RateLimitSummary',
    'ConsoleAdmin',
]
