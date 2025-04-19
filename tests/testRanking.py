from fastapi.testclient import TestClient
import pytest
from main import app

client = TestClient(app)

@pytest.mark.parametrize("test_case", [
    "when requesting \"/ranking\" endpoint with GET method and no parameters"
    "then should response with 200 ok and a json with \"ranking\" not empty"
])
def testGetRanking(test_case):
    response = client.get("/ranking")
    print(response.text)
    assert response.status_code == 200
    assert len(response.json()["funcionario"]) > 0