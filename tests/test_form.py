import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_index_get(client):
    response = client.get('/')
    assert response.status_code == 200

def test_index_post_valid_input(client):
    data = {'x': 3, 'y': 5, 'z': 4}
    response = client.post('/', data=data)
    assert response.status_code == 200
    assert b'Solution' in response.data

def test_index_post_no_solution_input(client):
    data = {'x': 2, 'y': 5, 'z': 0}
    response = client.post('/', data=data)
    assert response.status_code == 200
    assert b'No Solution.' in response.data

def test_index_post_invalid_input(client):
    data = {'x': 'invalid', 'y': 5, 'z': 4}
    response = client.post('/', data=data)
    assert response.status_code == 200
    assert b'Values sent must be integer' in response.data
