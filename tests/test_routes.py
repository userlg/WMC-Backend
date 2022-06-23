import pytest

from tests import app


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def test_using_mongo(mongodb):
    db = mongodb['test_database']
    db.test.insert({'username': 'woof',  'password': '12345abcd'})
    documents = db.test.find_one()
    return db


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello flask"
