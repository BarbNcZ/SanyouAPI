from fastapi.testclient import TestClient
import pytest
from main import app

client = TestClient(app)

@pytest.mark.parametrize("test_case", [
    "when requesting \"/departamentos\" endpoint with GET method and no parameters"
    "then should response with 200 ok and a json with \"depto\" not empty",
])
def testGetDepartamento(test_case):
    response = client.get("/departamentos")
    assert response.status_code == 200
    assert len(response.json()["depto"]) > 0