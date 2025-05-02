from fastapi.testclient import TestClient
import pytest
from main import app

client = TestClient(app)

@pytest.mark.parametrize("test_case", [
    "when requesting \"/charttaskperrole\" endpoint with GET method and no parameters"
    "then should response with 200 ok and a json with \"charttaskperrole\" not empty"
])
def testGetChartTaskPerRole(test_case):
    response = client.get("/charttaskperrole")
    print(response.text)
    assert response.status_code == 200
    assert len(response.json()["data"]) > 0



@pytest.mark.parametrize("test_case", [
    "when requesting \"/charttaskperdifficulty\" endpoint with GET method and no parameters"
    "then should response with 200 ok and a json with \"charttaskperdifficulty\" not empty"
])
def testGetChartTaskPerDifficulty(test_case):
    response = client.get("/charttaskperdifficulty")
    print(response.text)
    assert response.status_code == 200
    assert len(response.json()["data"]) > 0


