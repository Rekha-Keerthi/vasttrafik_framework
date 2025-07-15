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
class TestSearchTravel:
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
        print("test code for build trigger")

    @pytest.mark.smoke
    @pytest.mark.parametrize("test_list_item", test_list)
    def test_search_travel_planner(self, browserInstance, test_list_item):
        """Verifies search functionality in the travel planner.

        Args:
            test_list_item (dict): Contains 'from' and 'to' locations.
        """
        home_page = HomePage(browserInstance)
        home_page.travelplanner(
            test_list_item["from"], test_list_item["to"], "Jag vill resa nu"
        )
        print("Page title is:", home_page.getTitle())
        time.sleep(5)

    @pytest.mark.smoke
    @pytest.mark.parametrize("test_list_item", test_list)
    def test_search_travel_departuretime(self, browserInstance, test_list_item):
        """Verifies search functionality in the travel planner.

        Args:
            test_list_item (dict): Contains 'from' and 'to' locations.
        """
        browserInstance.refresh()
        home_page = HomePage(browserInstance)
        home_page.travelplanner(
            test_list_item["from"], test_list_item["to"], "Välj avgångstid", (11, 4, 5)
        )
        print("Page title is:", home_page.getTitle())
        print("test code to trigger build on code push")
        print("Testing")
        time.sleep(5)

    @pytest.mark.smoke
    @pytest.mark.parametrize("test_list_item", test_list)
    def test_search_travel_arrivaltime(self, browserInstance, test_list_item):
        """Verifies search functionality in the travel planner.

        Args:
            test_list_item (dict): Contains 'from' and 'to' locations.
        """
        browserInstance.refresh()
        home_page = HomePage(browserInstance)
        home_page.travelplanner(
            test_list_item["from"], test_list_item["to"], "Välj ankomsttid", (12, 6, 7)
        )
        print("Page title is:", home_page.getTitle())
        time.sleep(5)
