import pytest

from fixture.application import Application


fixture = None

@pytest.fixture()
def app(request):
    global fixture
    if fixture is None:
        browser = request.config.getoption("--browser")
        base_url = request.config.getoption("--baseUrl")
        fixture = Application(browser=browser, base_url=base_url)

        fixture.session.open_home_page()
        fixture.session.login(username="admin", password="secret")
    else:
        if not fixture.is_valid():
            browser = request.config.getoption("--browser")
            base_url = request.config.getoption("--baseUrl")
            fixture = Application(browser=browser, base_url=base_url)
        fixture.session.open_home_page()
        fixture.session.login(username="admin", password="secret")
    return fixture

@pytest.fixture(autouse=True)
def stop(request):
    def fin():
        if fixture is not None:
            fixture.finish()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--baseUrl", action="store", default="http://localhost:8090/addressbook/group.php")
