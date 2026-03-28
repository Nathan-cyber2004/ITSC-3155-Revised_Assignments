# Import statements
from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

def test_read_sheep():
    response = client.get(f"/sheep/{1}")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }

def test_add_sheep():
    response = client.post("/sheep/", json={
        "id": 99,
        "name": "Fluffy",
        "breed": "Merino",
        "sex": "ewe"
    })
    assert response.status_code == 201

    data = response.json()
    assert data["name"] == "Fluffy"
    assert data["breed"] == "Merino"
    assert data["sex"] == "ewe"
    assert "id" in data