from fastapi.testclient import TestClient
import pytest
from main import app

client = TestClient(app)

@pytest.mark.parametrize("test_case", [
    "when requesting \"/login\" endpoint with POST method and no parameters"
    "then should response with 200 ok and a json with \"login\" not empty",
])
def testLogin(test_case):

    payload = {
        "email": "asjhgdka@iaushdah.com",
        "password": '123456',
    }

    response = client.post("/login/", json=payload)
    print(response.text)

    assert response.status_code == 200
    assert len(response.json()["funcionario"]) > 0