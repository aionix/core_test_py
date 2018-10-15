import pytest

from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    fixture.session.open_home_page()
    fixture.session.login(username="admin", password="secret")
    request.addfinalizer(fixture.destroy)
    return fixture
