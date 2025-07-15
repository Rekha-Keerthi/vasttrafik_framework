import time
import os
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions

driver = None


# before requesting the command line options we need to register in the code, telling that these are options i can send from commands
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Send browser name as command line options",  # if the no browser_name options is not sent through commandd line , then default chrome option is used to run tests
    )


@pytest.fixture(scope="class")
def browserInstance(request):
    """we can run the chrome browser in Headless mode, meaning we can run the test script and script will invoke the broswer in backend so that user wont be able to see the browser invocation
    Selenium "wedriver" package provides a class called "ChromeOptions" which accepts the argument whter to run the browser in headless mode or not
    """

    "# we are activating the diver object and sending it back as global object to use in all the functions in the same file"

    global driver
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_argument("--disable-extensions")

    chrome_option.add_argument("--ignore-certificate-errors")
    chrome_option.add_argument("--start-maximized")
    # here fixture will receive browser name say:chrome as command line option
    browser_name = request.config.getoption("browser_name").lower()

    # whem the webdriver invokes the Chrome browser, provide the above chrome option as an argument, in what way to run the browser whether in headless or not
    if browser_name == "chrome":
        driver = webdriver.Chrome(
            options=chrome_option
        )  # Using selenium webdriver class and its Chrome() method create an object chrome browser object

    elif browser_name == "edge":
        driver = (
            webdriver.Edge()
        )  # Using selenium webdriver class and its Chrome() method create an object chrome browser object

    driver.get("https://www.vasttrafik.se/")

    yield driver
    driver.close()


# Hook into pytest-html to attach extra info
# @pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_header(cells):
    cells.insert(4, "<th>Time</th>")


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_row(cells):
    cells.insert(4, datetime.now().strftime("%H:%M:%S"))


# to get the screenshots of all the test failures
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    if report.when == "call" or report.when == "setup":
        xfail = hasattr(report, "wasxfail")
        if (
            (report.skipped and xfail)
            or (report.failed and not xfail)
            or (report.passed and not xfail)
        ):

            # file_name = report.nodeid.replace("::", "_") + ".png"
            item_name = report.nodeid.replace("::", "_") + ".png"
            file_name = get_screenshot_and_save(item_name)

            if (
                file_name
            ):  # this line code is used to attach the screenshot to the html report
                html = (
                    '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" '
                    'onclick="window.open(this.src)" align="right"/></div>' % item_name
                )

                extras.append(pytest_html.extras.html(html))
        report.extras = extras


def get_screenshot_and_save(name):
    screenshots_dir = "reports"
    os.makedirs(screenshots_dir, exist_ok=True)
    filepath = os.path.join(screenshots_dir, name)
    driver.get_screenshot_as_file(filepath)
    return filepath
