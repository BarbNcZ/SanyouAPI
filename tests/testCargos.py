from fastapi.testclient import TestClient
import pytest
from main import app

client = TestClient(app)

@pytest.mark.parametrize("test_case", [
    "when requesting \"/cargo\" endpoint with GET method and no parameters"
    "then should response with 200 ok and a json with \"cargo\" not empty",
])
def testGetCargo(test_case):
    response = client.get("/cargo")
    assert response.status_code == 200
    assert len(response.json()["cargo"]) > 0