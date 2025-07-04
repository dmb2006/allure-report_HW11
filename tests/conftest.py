import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def browser_configuration():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 7

    yield

    browser.quit()