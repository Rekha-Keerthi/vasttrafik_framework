import inspect
import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.select import Select


class BaseClass:
    """Class consists of functions which are commonly used in testing across all files and classes
    * Contains logging method to invoke across all child classes
    * Contains a method to verifying current url of the page on navigation
    * Contains a method to verifying title of the current page
    * Contains Explicit wait functions to locate web element on the web page for desired amount of time

    """

    def __init__(self, driver):
        self.driver = driver

        "Locators for Tavel Planner input fields"
        self.taverlplanner_header = (By.TAG_NAME, "//h1")
        self.from_element = (By.CSS_SELECTOR, "#from-to-selector-from")
        self.to_element = (By.CSS_SELECTOR, "#from-to-selector-to")
        self.from_listoflocations = (
            By.CSS_SELECTOR,
            "ul[id='autocomplete-results-from-to-selector-from'] li span:nth-child(2)",
        )
        self.towards_listoflocations = (
            By.CSS_SELECTOR,
            "ul[id='autocomplete-results-from-to-selector-to'] li span:nth-child(2)",
        )

        "travel planner start page "
        self.travelplanner_startpage = (
            By.XPATH,
            "(//div[@class='col-lg-8']/div/div)[2]",
        )
        self.day_locator = (By.XPATH, "//select[@class='w-100 ms-0 me-0 form-select ']")

        self.time_hour_locator = (
            By.XPATH,
            "//div[@class='w-50 me-1 d-none d-sm-block']/select",
        )
        self.time_mins_locator = (
            By.XPATH,
            "//div[@class='w-50 ms-1 d-none d-sm-block']/select",
        )

        self.search_button = (By.CSS_SELECTOR, "#searchbutton")
        self.change_direction_arrows = (By.XPATH, "//button[@title='Ändra riktning']")

        # Västraffik Logo locator
        self.västraffiklogo = (By.CSS_SELECTOR, ".header-desktop__logo")

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        if not logger.handlers:
            fileHandler = logging.FileHandler("logfile.log")
            formatter = logging.Formatter(
                "%(asctime)s :%(levelname)s : %(name)s :%(message)s"
            )
            fileHandler.setFormatter(formatter)

            logger.addHandler(fileHandler)  # filehandler object

            logger.setLevel(logging.INFO)
        return logger

    def getTitle(self):
        return self.driver.title

    def getCurrentUrl(self):
        return self.driver.current_url

    def fill_from_location(self, location_text, default_from="Bellevue, Göteborg"):

        self.verify_Element_Presence_Located(self.from_element).send_keys(location_text)
        list_of_from_locations = self.verify_Elements_Presence_Located(
            self.from_listoflocations
        )
        for list_of_from_location in list_of_from_locations:
            if list_of_from_location.text == default_from:
                list_of_from_location.click()
                break
        from_location_selected = self.driver.find_element(
            *self.from_element
        ).get_attribute("value")
        return from_location_selected

    def fill_to_location(self, location_text, default_to="Nordstan, Göteborg"):

        self.verify_Element_Presence_Located(self.to_element).send_keys(location_text)
        list_of_towards_locations = self.verify_Elements_Presence_Located(
            self.towards_listoflocations
        )
        for list_of_towards_location in list_of_towards_locations:

            if list_of_towards_location.text == default_to:
                list_of_towards_location.click()
                break
        till_location_selected = self.driver.find_element(
            *self.to_element
        ).get_attribute("value")
        return till_location_selected

    def set_travel_time(self, day_index, hour_index, minute_index):
        date_field = self.verify_Element_Presence_Located(self.day_locator)
        date_dropdown = Select(date_field)
        date_dropdown.select_by_index(day_index)
        date_selected = date_dropdown.first_selected_option
        print("Date selected from dropdown is ", date_selected.text)
        time_hours_field = self.verify_Element_Presence_Located(self.time_hour_locator)
        time_mins_field = self.verify_Element_Presence_Located(self.time_mins_locator)
        time_hours_dropdown = Select(time_hours_field)
        time_hours_dropdown.select_by_index(hour_index)
        time_mins_dropdown = Select(time_mins_field)
        time_mins_dropdown.select_by_index(minute_index)

    def when_will_you_travel(self, travelling_when):
        travel_time_layout = self.driver.find_element(*self.travelplanner_startpage)

        # verify the text När vill du resa?
        travel_time_text = travel_time_layout.find_element(
            By.XPATH, "div/fieldset/legend"
        ).text
        assert travel_time_text == "När vill du resa?", "texts do match"

        "verify radio button selection during travel search"
        travel_time_options = travel_time_layout.find_elements(
            By.XPATH, "div/fieldset/div/label"
        )
        for travel_time_option in travel_time_options:
            if travel_time_option.text == travelling_when:
                travel_time_option.click()
                break
                # calling methods to select date from and time for travel search"
        return travel_time_option

    def travelplanner(
        self,
        from_input,
        till_input,
        travelling_when="Välj avgångstid",
        time_d_h_m=(10, 2, 3),
    ):
        from_location_selected = self.fill_from_location(from_input)
        till_location_selected = self.fill_to_location(till_input)
        self.when_will_you_travel(travelling_when)
        # On selecting radio option check whether travel time dropdowns are displayed

        date_field_element = self.driver.find_elements(*self.day_locator)

        print("When will you travel: " + travelling_when)
        if date_field_element:
            self.set_travel_time(time_d_h_m[0], time_d_h_m[1], time_d_h_m[2])

        self.verify_Element_Presence_Located(self.search_button).click()
        print(
            "From_locattion is: " + from_location_selected,
            " and to_location is: " + till_location_selected,
        )
        change_directions = self.verify_Element_Presence_Located(
            self.change_direction_arrows
        )
        change_directions.click()
        print("Clicked on Ändra riktning icon to reverse the from and to locations.")
        from_location_selected = self.verify_Element_Presence_Located(
            self.from_element
        ).get_attribute("value")
        till_location_selected = self.verify_Element_Presence_Located(
            self.to_element
        ).get_attribute("value")
        print(
            "From_locattion is: " + from_location_selected,
            " and to_location is: " + till_location_selected,
        )
        print(end="\n")
        self.verify_Element_Presence_Located(self.search_button).click()

    def click_on_västraffik_logo(self):
        """Function to check whether the page is refreshed and user is landed to Home Page when clicked on Västraffik log
        Returns:
            webpage link: returns current url of the vasttraffic home page
        """

        self.driver.find_element(*self.västraffiklogo).click()
        url_onpage_refresh = self.getCurrentUrl()

        return url_onpage_refresh

    def verify_Element_Presence_Located(self, locator_path):
        """Function to explicitly wait to locate the element on webpage for specified time
        Args:
            locator_path (tuple): functions accepts tuple as a argument
        Returns:
            WebElement: returns the web element located on X and Y axis
        """

        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(locator_path)
        )

        return element

    def verify_Elements_Presence_Located(self, elements_path):
        """Function to explicitly wait to locate the element on webpage for specified time
        Args:
            locator_path (tuple): functions accepts tuple as a argument with locator type and locator value
        Returns:
            WebElements: returns tha list of web elements located on X and Y axis
        """

        elements = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_all_elements_located(elements_path)
        )

        return elements
