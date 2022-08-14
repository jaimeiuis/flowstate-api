import pytest

from flowstate.app import create_app


@pytest.yield_fixture(scope='session')
def app():
    """ Set up Flask app once per testing session. """
    params = {
        'DEBUG': False,
        'TESTING': True,
    }

    _app = create_app(settings_override=params)

    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.yield_fixture(scope='function')
def client(app):
    """ Setup an app client once per testing function. """
    yield app.test_client()