from selenium.webdriver.common.by import By

from utilities.baseclass import BaseClass


class ReseplaneringPage(BaseClass):
    """Page Object for 'Reseplanering' page that handles trip planning interactions.

    Args:
        BaseClass (class): Inherits methods from the base Selenium wrapper class.
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.triptypes = (
            By.XPATH,
            "(//div[@class='link-block position-relative']/div/a)",
        )
        self.reseplaneraren_heading = (
            By.CSS_SELECTOR,
            "div[class='mb-3 pt-md-3'] div h1",
        )

        self.heading_info = (By.XPATH, "(//div[@class='mb-3 pt-md-3']/div)[2]/p")

    def trip_types(self, from_loc, to_loc):
        """Navigates to the 'Reseplaneraren' section and performs a travel search.

        Args:
            from_loc (str): Starting location.
            to_loc (str): Destination location.

        Returns:
            str: Heading info text related to trip planning.
        """
        new_text = ""
        types_of_trips_booking_list = self.driver.find_elements(*self.triptypes)

        for trip_type in types_of_trips_booking_list:
            if trip_type.get_attribute("title") == "Reseplaneraren":
                trip_type.click()
                self.travelplanner(from_loc, to_loc)
                break

        self.verify_Elements_Presence_Located(self.heading_info)
        heading_paragraph = self.driver.find_elements(*self.heading_info)
        for header_text in heading_paragraph:
            p_text = header_text.text
            new_text = new_text + p_text

        return "Reseplaneraren_info: " + new_text
