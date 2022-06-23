

import pytest

from app import create_app

from pytest_dbfixtures import factories

mongo_proc2 = factories.mongo_proc(port=27017, params='--nojournal --noauth --nohttpinterface --noprealloc')
mongodb2 = factories.mongodb('mongo_proc2')

'''
@pytest.fixture
def client():
    return app.test_client()

def test_home(client):
   response = client.get('/')
   assert response.status_code == 200
   #assert isinstance(resp.json, dict)
   assert response.data == b'Hello flask'
'''

@pytest.fixture
def app():
    app = create_app()
    return app


