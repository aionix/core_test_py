import json

import pytest

from fixture.application import Application


fixture = None

@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    with open(request.config.getoption("--target")) as config_file:
        target = json.load(config_file)
    base_url = target["baseUrl"]
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target['baseUrl'])
        fixture.session.open_home_page()
        fixture.session.login(username=target['username'], password=target['password'])
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
    parser.addoption("--target", action="store", default="target.json")

@pytest.fixture()
def attach_screen(request):
    yield True
