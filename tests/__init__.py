import pytest

import warnings

from app import create_app


@pytest.fixture
def app():
    app = app.create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )
    #yield app
    return app


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()



