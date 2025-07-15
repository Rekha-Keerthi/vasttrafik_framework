import json
import time

import pytest
from pageobjects.home_page import HomePage

from pathlib import Path

workspace_root = Path(__file__).resolve().parent.parent
test_data_path = workspace_root / "data" / "test_vasttrafic_home.json"

with open(test_data_path) as inputdata:
    test_data = json.load(
        inputdata
    )  # json load method reads the json file to python object
    test_list = test_data["data"]


@pytest.mark.usefixtures("browserInstance")
class TestHomePage:
    """Test suite for verifying key functionalities on the Västtrafik homepage."""

    def test_cookie_container(self, browserInstance):
        """Verifies the cookie consent popup and simulates user approval.

        Args:
            browserInstance (fixture): Returns the initialized WebDriver instance.
        """
        # browserInstance fixture is retuning driver

        home_page = HomePage(browserInstance)
        log = home_page.getLogger()
        user_approved = home_page.cookie_container()
        log.info("User clicked on : %s  button", user_approved)

    @pytest.mark.parametrize("test_list_item", test_list)
    def test_traffic_situation(self, browserInstance, test_list_item):
        """
        Verifies municipality search and selection.

        Args:
            test_list_item (dict): Contains 'municipal' and 'town' values.
        """
        home_page = HomePage(browserInstance)
        log = home_page.getLogger()
        user_selected_municipal = home_page.search_municipality(
            test_list_item["municipal"], test_list_item["town"]
        )
        log.info(
            "User has selected the following municipalities: %s ",
            user_selected_municipal,
        )
        print("testing build on code push")
        time.sleep(3)

    def test_news_advertised(self, browserInstance):
        """Verifies that news headlines are displayed and navigates to 'Fler nyheter' section."""

        browserInstance.execute_script("window.scrollTo(0,900);")
        home_page = HomePage(browserInstance)
        log = home_page.getLogger()
        news_headlines = home_page.moveto_news_section()
        log.info("News Headlines are: %s", str(news_headlines))
        time.sleep(5)

    def test_traffic_content_area(self, browserInstance):
        """Verifies navigation to the 'Biljetter' section and retrieves Enkelbiljetter information."""

        home_page = HomePage(browserInstance)
        home_page.click_on_västraffik_logo()
        enkelbiljetter_info = home_page.traffic_contentarea()
        log = home_page.getLogger()
        log.info("User has navigated to EnkelBiljetter Page: %s", enkelbiljetter_info)
        time.sleep(3)

    @pytest.mark.parametrize("test_list_item", test_list)
    def test_homepage_header_list(self, browserInstance, test_list_item):
        """Verifies header menu interaction and Reseplanering navigation.

        Args:
            test_list_item (dict): Contains 'from' and 'to' locations.
        """
        home_page = HomePage(browserInstance)
        log = home_page.getLogger()
        Reseplaneraren_header_info = home_page.homepage_header_list(
            test_list_item["from"], test_list_item["to"]
        )
        log.info(
            "User has navigated to Reseplaneraren Page: %s", Reseplaneraren_header_info
        )
        time.sleep(3)
