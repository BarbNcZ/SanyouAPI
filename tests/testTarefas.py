from fastapi.testclient import TestClient
import pytest
from main import app

client = TestClient(app)

@pytest.mark.parametrize("test_case", [
    "when requesting \"/createtarefa\" endpoint with PUT method and parameters \"/1/repor%20setor%20de%20bebidas\", "
    "then should response with 200 ok and a json with \"id_tarefa\" higher than 0",
])
def testCreateTarefa(test_case):
    response = client.put("/createtarefa/1/repor%20setor%20de%20bebidas/5")
    assert response.status_code == 200
    assert response.json()["id_tarefa"] > 0


@pytest.mark.parametrize("test_case", [
    "when requesting \"/tarefas\" endpoint with GET method and no parameters, "
    "then should response with 200 ok and a json with \"tarefas\" not empty",
])
def testGetTarefas(test_case):
    response = client.get("/tarefas")
    assert response.status_code == 200
    assert len(response.json()["tarefas"]) > 0

# WARNING! THIS WILL DELETE THE TASK FROM DATABASE!
"""
@pytest.mark.parametrize("test_case", [
    "when requesting \"/deletetarefa\" endpoint with DELETE method and parameter \"/1\", "
    "then should response with 200 ok and a json with \"result\" as True",
])
def testDeleteTarefa(test_case):
    response = client.delete("/deletetarefa/1")
    assert response.status_code == 200
    assert response.json()["result"] == True
"""