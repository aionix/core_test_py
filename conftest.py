import json
import time

import allure
import pytest
from allure_commons.types import AttachmentType

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


@pytest.mark.tryfirst
def pytest_runtest_makereport(item, call, __multicall__):
    rep = __multicall__.execute()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture(scope="function", autouse=True)
def screenshot_on_failure(request):
    def fin():
        if request.node.rep_setup.failed:
            allure.attach(fixture.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        elif request.node.rep_setup.passed:
            if request.node.rep_call.failed:
                allure.attach(fixture.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    request.addfinalizer(fin)


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        if fixture is not None:
            fixture.finish()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")


