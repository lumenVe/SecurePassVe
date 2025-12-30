# Test to ensure debug routes are disabled in production environment

import pytest

@pytest.mark.parametrize(
    "path",
    [
        "/api/v1/debug/error",
        "/api/v1/debug/echo?message=hello&times=3",
    ],
)

def test_debug_endpoints_disabled_in_prod(prod_client, path: str):
    resp = prod_client.get(path)
    assert resp.status_code == 404

    data = resp.json()
    assert data["error"] == "not_found"
