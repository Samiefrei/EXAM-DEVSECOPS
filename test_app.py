import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json()['status'] == 'healthy'

def test_add_item(client):
    response = client.post('/items', json={"name": "Clavier", "quantity": 5})
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == "Clavier"
    assert data['quantity'] == 5

def test_add_item_missing_name(client):
    response = client.post('/items', json={"quantity": 1})
    assert response.status_code == 400
