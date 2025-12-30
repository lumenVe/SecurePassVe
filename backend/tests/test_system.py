def test_health_endpoint(prod_client: TestClient):
    response = prod_client.get("/api/v1/health")
    assert response.status_code == 200
    assert "status" in response.json()

def test_meta_endpoint(prod_client: TestClient):
    response = prod_client.get("/api/v1/meta")
    assert response.status_code == 200
    json_response = response.json()
    assert "version" in json_response
    assert "env" in json_response

def test_404_uses_unified_error_format(prod_client: TestClient):
    response = prod_client.get("/api/v1/nonexistent")
    assert response.status_code == 404
    
    json_response = response.json()
    assert "error" in json_response
    assert "message" in json_response
    assert json_response["error"] == "not_found"