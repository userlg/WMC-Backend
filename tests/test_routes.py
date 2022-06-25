import pytest



def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello flask"



def test_home2(client):
   response = client.get('/about')
   assert response.status_code == 200
   #assert isinstance(resp.json, dict)
   assert response.data == b'About Route'
