"""Round-trip tests for the *Summary wire-format projections.

These models are the contract between the gatekeeper-backend admin endpoints
and any consumer (frontend console, api-gatekeeper-api-python, mcp-gatekeeper).
to_dict() emits JSON-ready output; from_dict() reverses it. The round-trip
tests guard against either side drifting from the other.
"""
import pytest

from api_gatekeeper_models import (
    ClientStatus,
    ClientSummary,
    HttpMethod,
    PermissionSummary,
    RateLimitSummary,
)


def test_client_summary_roundtrip() -> None:
    original = ClientSummary(
        client_id="client-uuid-1",
        client_name="test-client",
        status=ClientStatus.ACTIVE,
        api_key_masked="abcd1234…wxyz",
        created_at=1_700_000_000,
        updated_at=1_700_000_500,
    )
    restored = ClientSummary.from_dict(original.to_dict())
    assert restored == original


def test_client_summary_from_dict_status_string_to_enum() -> None:
    data = {
        "client_id": "c1",
        "client_name": "n",
        "status": "suspended",
        "api_key_masked": "x",
        "created_at": 0,
        "updated_at": 0,
    }
    summary = ClientSummary.from_dict(data)
    assert summary.status is ClientStatus.SUSPENDED


def test_client_summary_from_dict_rejects_unknown_status() -> None:
    data = {
        "client_id": "c1",
        "client_name": "n",
        "status": "not-a-real-status",
        "api_key_masked": "x",
        "created_at": 0,
        "updated_at": 0,
    }
    with pytest.raises(ValueError):
        ClientSummary.from_dict(data)


def test_client_summary_from_dict_missing_field_raises() -> None:
    with pytest.raises(KeyError):
        ClientSummary.from_dict({"client_id": "c1"})


def test_permission_summary_roundtrip() -> None:
    original = PermissionSummary(
        permission_id="perm-uuid-1",
        client_id="client-uuid-1",
        client_name="test-client",
        route_id="route-uuid-1",
        route_domain="api.example.com",
        route_pattern="/users/*",
        route_service_name="users-svc",
        allowed_methods=[HttpMethod.GET, HttpMethod.POST],
        created_at=1_700_000_000,
    )
    restored = PermissionSummary.from_dict(original.to_dict())
    assert restored == original


def test_permission_summary_from_dict_methods_string_list_to_enums() -> None:
    data = {
        "permission_id": "p1",
        "client_id": "c1",
        "client_name": "n",
        "route_id": "r1",
        "route_domain": "d",
        "route_pattern": "/p",
        "route_service_name": "s",
        "allowed_methods": ["GET", "DELETE"],
        "created_at": 0,
    }
    summary = PermissionSummary.from_dict(data)
    assert summary.allowed_methods == [HttpMethod.GET, HttpMethod.DELETE]


def test_permission_summary_from_dict_rejects_unknown_method() -> None:
    data = {
        "permission_id": "p1",
        "client_id": "c1",
        "client_name": "n",
        "route_id": "r1",
        "route_domain": "d",
        "route_pattern": "/p",
        "route_service_name": "s",
        "allowed_methods": ["GET", "FROBNICATE"],
        "created_at": 0,
    }
    with pytest.raises(ValueError):
        PermissionSummary.from_dict(data)


def test_rate_limit_summary_roundtrip() -> None:
    # RateLimitSummary.from_dict() pre-existed — round-trip test added for
    # symmetry with the other two summary models.
    original = RateLimitSummary(
        client_id="client-uuid-1",
        client_name="test-client",
        requests_per_day=10_000,
        created_at=1_700_000_000,
        updated_at=1_700_000_500,
    )
    restored = RateLimitSummary.from_dict(original.to_dict())
    assert restored == original
