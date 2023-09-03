import pytest
from app import app
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_api_get(client):
    query_parameters = {'x': 3, 'y': 5, 'z': 4}
    response = client.get('/api', query_string=query_parameters)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'parameters' in data
    assert 'solution' in data

def test_api_no_solution_input(client):
    query_parameters = {'x': 2, 'y': 5, 'z': 0}
    response = client.get('/api', query_string=query_parameters)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'parameters' in data
    assert 'solution' in data
    assert 'No Solution.' in data['solution']

def test_api_invalid_input(client):
    query_parameters = {'x': 'invalid', 'y': 5, 'z': 4}
    response = client.get('/api', query_string=query_parameters)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'error' in data
    assert 'Values sent must be integer' in data['error']
