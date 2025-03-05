from fastapi.testclient import TestClient
import pytest
from main import app

client = TestClient(app)

@pytest.mark.parametrize("test_case", [
    "when requesting \"/tipotarefa\" endpoint with GET method and no parameters"
    "then should response with 200 ok and a json with \"tipo_tarefa\" not empty",
])
def testGetTipoTarefa(test_case):
    response = client.get("/tipotarefa")
    assert response.status_code == 200
    assert len(response.json()["tipo_tarefa"]) > 0