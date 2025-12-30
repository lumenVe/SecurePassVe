import importlib
import os

import pytest
from fastapi.testclient import TestClient

@pytest.fixture
def prod_client() -> TestClient:
    os.environ["SECUREPASSVE_ENV"] = "prod"
    
    import securepassve_backend.main as main
    importlib.reload(main)
    
    return TestClient(main.app)