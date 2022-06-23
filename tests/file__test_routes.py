import pytest



@pytest.fixture
def client():
    return app.test_client()

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200








'''
#def test_home(client):
#   resp = client.get('/')
#   assert resp.status_code == 200
#  assert isinstance(resp.json, dict)
#   assert resp.json.get('message', 'Hello flask')


'''

'''


import pytest
from app import app


@pytest.fixture
def client():
    return app.test_client()

def test_service(client):
    resp = client.post('/service', json={'email_address': 'some@thing.com', 'username': 'mehdi'})
    assert resp.status_code == 200
    assert resp.json.get('success')

def test_service_bad_http_method(client):
    resp = client.get('/service')
    assert resp.status_code == 405

def test_service_no_json_body(client):
    resp = client.post('/service', data='something')
    assert resp.status_code == 400
    assert not resp.json.get('success')

def test_service_missing_email(client):
    resp = client.post('/service', json={'username': 'mehdi'})
    assert resp.status_code == 400
    assert not resp.json.get('success')


'''