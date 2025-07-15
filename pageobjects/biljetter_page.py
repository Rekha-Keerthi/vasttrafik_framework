from selenium.webdriver.common.by import By

from utilities.baseclass import BaseClass


class BiljetterPage(BaseClass):
    """Page Object Model for the 'Biljetter' page.
    Provides methods to interact with and retrieve information about available ticket types.

    Inherits:
        BaseClass: Provides shared Selenium utilities.
    """

    def __init__(self, driver):
        """Initializes locators for the types of tickets available on Biljetter page.

        Args:
            driver: Selenium Webdriver instance
        """
        super().__init__(driver)
        self.driver = driver

        self.tickettypes = (
            By.XPATH,
            "(//div[@class='link-block position-relative']/div/a)",
        )
        self.enkelbiljetter_information = (
            By.CSS_SELECTOR,
            "div[class='page-introduction page-introduction--sub fullwidth-xs p-3 p-sm-4 print-reset'] p:nth-child(1)",
        )  # (div[class=singleticket-search-page"] div div div p[1]

    def biljetter_ticket_types(self, ticket_name="Enkelbiljetter"):
        """
        Clicks on the 'Enkelbiljetter' ticket type and retrieves its introductory text.

        Returns:
            str: Header or introduction text for 'Enkelbiljetter'.
        """

        types_of_tickets_booking_list = self.driver.find_elements(*self.tickettypes)

        for ticket_type in types_of_tickets_booking_list:
            if ticket_name in ticket_type.get_attribute("title"):
                ticket_type.click()
                break
        enkelbiljetter_header_text = self.verify_Element_Presence_Located(
            self.enkelbiljetter_information
        ).text

        return enkelbiljetter_header_text
