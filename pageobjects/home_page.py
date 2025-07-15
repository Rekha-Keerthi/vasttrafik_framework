import time

from selenium.webdriver.common.by import By

from pageobjects.biljetter_page import BiljetterPage
from pageobjects.reseplanering_page import ReseplaneringPage
from utilities.baseclass import BaseClass


class HomePage(BaseClass):
    """Page Object Model class for the homepage.
    This class includes locators and methods to interact with key homepage elements such as:
        - Municipality search
        - Cookie handling
        - Traffic content navigation
        - Header menu navigation
        - News section interaction

    Inherits:
        BaseClass: Provides shared Selenium utilities and logging.
    """

    # Inheriting BaseClass to get title of the current page object classes

    def __init__(self, driver):
        """Class Constructor : Contains a locators for web elements in the form of tuple containing locator type and locator path
        * Initializing driver object to parent class "BaseClass" init  to access its methods and properties

        Args:
            driver : Webdriver object returned from browserInstance setup fixture
        """

        super().__init__(driver)

        self.driver = driver
        self.log = self.getLogger()

        self.headerlist = (
            By.CSS_SELECTOR,
            'div[class="d-none d-md-block"] div div div nav ul li div  a',
        )

        "travel planner search grid locator on home page "
        self.travelplanner_startpage = (
            By.XPATH,
            "(//div[@class='col-lg-8']/div/div)[2]",
        )

        "Locators for Cookie Popup"
        self.anpassa_kakor = (
            By.XPATH,
            "(//div[@class='container container--wider']/div/div)[2]/a",
        )

        self.approve_buttons = (
            By.XPATH,
            "(//div[@class='container container--wider']/div/div)[2]/button",
        )

        "Locator of traffic content area"
        self.traffic_content_area = (
            By.CSS_SELECTOR,
            "div[class='row row-cols-1 row-cols-md-4'] div div div a div div:nth-child(2)",
        )

        "locator to search community input field "
        self.search_municipal = (By.XPATH, "//input[@id='municipality-selector']")

        "locator to get the list of municipalities listed in dropdown"
        self.municipality_search_list = (
            By.XPATH,
            "//div[@class='autocomplete rounded d-flex flex-nowrap flex-grow-1 align-items-center  position-relative']/ul/li",
        )

        "locator to get the municipality displayed from dropdown selection"
        self.municipality_selected = (
            By.XPATH,
            "//div[@class='municipality-selector__selected-municipalities d-flex flex-row flex-wrap']/button",
        )

        self.traffic_information = (By.XPATH, "//div[@role='listitem']/a")

        "locator to get the news headline displayed on home page"
        self.news_section = (
            By.XPATH,
            "//div[@class='news-block row row-cols-1 row-cols-md-3']/div/a/div/h3",
        )

    def cookie_container(self):
        """Clicks the 'GODKÄNN ALLA' button on the cookie popup if present.
        Returns:
            str: The button text if clicked, otherwise nothing.
        Exceptions:
            Prints a message if the popup is not found or already handled.
        """
        cookie_button_types = []

        try:

            anpassa_kakor_button = self.verify_Element_Presence_Located(
                self.anpassa_kakor
            )
            cookie_button_types.append(anpassa_kakor_button)
            approve_buttons = self.verify_Elements_Presence_Located(
                self.approve_buttons
            )
            cookie_button_types.extend(approve_buttons)
            for button_type in cookie_button_types:
                button_text = button_type.get_attribute("innerText").strip()
                if button_text == "GODKÄNN ALLA":
                    button_type.click()
                    return button_text
            return None
        except Exception as e:
            print("Cookie popup not found or already accepted:", e)

    def search_municipality(self, municipal_input="Gö", target_municipality="Göteborg"):
        """Selects the given municipality from the search results and verifies the selection.
        Args:
            municipal_input (str): Text to input in the municipality search box.
            target_municipality (str): Name of the municipality to select.

        Returns:
            str: The name of the selected municipality.
        """

        municipality_search_box = self.verify_Element_Presence_Located(
            self.search_municipal
        )
        municipality_search_box.send_keys(municipal_input)
        municipalities_search_result = self.verify_Elements_Presence_Located(
            self.municipality_search_list
        )
        for municipality in municipalities_search_result:
            if municipality.text == target_municipality:
                municipality.click()
                break
        user_selected_municipalities = self.driver.find_elements(
            *self.municipality_selected
        )
        for municipalities_selected in user_selected_municipalities:
            if municipalities_selected.text == target_municipality:
                # traffic_information_list = self.driver.find_elements(*self.traffic_information)"
                return municipalities_selected.text
            else:
                return municipalities_selected.text

    def traffic_contentarea(self):
        """Clicks on the 'Biljetter' section from the traffic content areas and returns ticket info.
        Returns:
            str: Header information from the 'Enkelbiljetter' section.
        """
        traffic_contenareas = self.verify_Elements_Presence_Located(
            self.traffic_content_area
        )

        for traffic_type in traffic_contenareas:
            if traffic_type.text == "Biljetter":
                traffic_type.click()
                break
        biljetter_page = BiljetterPage(self.driver)
        enkelbiljetter_info = biljetter_page.biljetter_ticket_types()
        return enkelbiljetter_info

    def homepage_header_list(self, fromlocation, tolocation):
        """Clicks on the 'Reseplanering' header item and returns trip planning information.
        Args:
            fromlocation (str): Starting location.
            tolocation (str): Destination location.

        Returns:
            str: Trip type information from the Reseplaneraren page.
        """
        header_list = self.driver.find_elements(*self.headerlist)
        # Iterating throw each items on the header list
        for header_item in header_list:
            # Checking if the retrieved webelement text matches with given text
            if header_item.text == "Reseplanering":
                header_item.click()  # click on the link
                break
        resplanering_page = ReseplaneringPage(self.driver)

        reseplaneraren_page_info = resplanering_page.trip_types(
            fromlocation, tolocation
        )
        return reseplaneraren_page_info

    def moveto_news_section(self):
        """Collects current news headlines and clicks the 'Fler nyheter' (More news) link.
        Returns:
            list: A list of current news headline texts.
        """
        news_headline = []
        current_news_displayed = self.driver.find_elements(*self.news_section)
        for news_item in current_news_displayed:
            news_headline.append(news_item.text)
        more_news = self.verify_Element_Presence_Located((By.LINK_TEXT, "Fler nyheter"))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", more_news)
        self.driver.execute_script("arguments[0].click();", more_news)
        time.sleep(3)
        return news_headline
