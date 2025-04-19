from fastapi.testclient import TestClient
import pytest
from main import app

client = TestClient(app)

@pytest.mark.parametrize("test_case", [
    "when requesting \"/funcionarios\" endpoint with GET method and no parameters"
    "then should response with 200 ok and a json with \"funcionarios\" not empty"
])
def testGetFuncionarios(test_case):
    response = client.get("/funcionarios")
    print(response.text)
    assert response.status_code == 200
    assert len(response.json()["funcionario"]) > 0


@pytest.mark.parametrize("test_case", [
    "when requesting \"/createfuncionario\" endpoint with PUT method and parameters \"/1/1/any@email.com/Kevin\", "
    "then should response with 200 ok and a json with \"cd_funcionario\" higher than 0",
])
def testCreateFuncionario(test_case):
    response = client.put("/createfuncionario/1/1/any@email.com/Kevin")
    assert response.status_code == 200
    assert response.json()["cd_funcionario"] > 0


"""@pytest.mark.parametrize("test_case", [
    "when requesting \"/deletefuncionario\" endpoint with DELETE method and parameter \"/1\", "
    "then should response with 200 ok and a json with \"result\" as True"
])
def testDeleteFuncionario(test_case):
    response = client.delete("/deletefuncionario/25")
    assert response.status_code == 200
    assert response.json()["result"] == True
"""