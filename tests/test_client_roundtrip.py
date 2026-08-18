"""Roundtrip tests for the Client dataclass to lock the from_dict/to_dict contract."""
from api_gatekeeper_models import Client, ClientStatus


def _base_row(**overrides) -> dict:
    row = {
        'client_id': 'c0b4b615-2381-48ff-935b-6c56596abda6',
        'client_name': 'Podcast Guru BoostMeta Mobile Client',
        'shared_secret': 'shhh',
        'api_key': None,
        'status': 'active',
        'created_at': 1786807635,
        'updated_at': 1786807635,
        'legacy_key_id': None,
    }
    row.update(overrides)
    return row


def test_client_roundtrip_without_legacy_key_id() -> None:
    row = _base_row()
    client = Client.from_dict(row)
    assert client.legacy_key_id is None
    assert client.to_dict() == row


def test_client_roundtrip_with_legacy_key_id() -> None:
    row = _base_row(legacy_key_id='podcastguru-mobile')
    client = Client.from_dict(row)
    assert client.legacy_key_id == 'podcastguru-mobile'
    assert client.to_dict() == row


def test_client_from_dict_tolerates_missing_legacy_key_id_key() -> None:
    row = _base_row()
    del row['legacy_key_id']
    client = Client.from_dict(row)
    assert client.legacy_key_id is None


def test_client_create_new_defaults_legacy_key_id_to_none() -> None:
    client = Client.create_new(client_name='new client', shared_secret='s')
    assert client.legacy_key_id is None


def test_client_create_new_accepts_legacy_key_id() -> None:
    client = Client.create_new(
        client_name='legacy client',
        shared_secret='s',
        legacy_key_id='legacy-str',
    )
    assert client.legacy_key_id == 'legacy-str'
    assert client.to_dict()['legacy_key_id'] == 'legacy-str'


def test_client_status_active_defaults_serialize_correctly() -> None:
    client = Client.create_new(client_name='c', api_key='k', status=ClientStatus.SUSPENDED)
    d = client.to_dict()
    assert d['status'] == 'suspended'
    assert 'legacy_key_id' in d
