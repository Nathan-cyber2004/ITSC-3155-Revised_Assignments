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
    new_sheep = {
        "id": 99,
        "name": "Fluffy",
        "breed": "Gotland",
        "sex": "ewe"
    }

    response = client.post("/sheep/", json=new_sheep)

    assert response.status_code == 201

    data = response.json()
    assert data["name"] == "Fluffy"
    assert data["breed"] == "Gotland"
    assert data["sex"] == "ewe"
    assert "id" in data

    # Verify the sheep was actually added by retrieving it by ID
    get_response = client.get("/sheep/99")
    assert get_response.status_code == 200
    assert get_response.json() == new_sheep