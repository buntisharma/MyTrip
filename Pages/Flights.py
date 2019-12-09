from Library import ConfigReader
import time

class test_bookair():
    def __init__(self, driver):
        self.driver = driver

    def test_searchflights(self):
        self.driver.find_element_by_css_selector(ConfigReader.test_homeloc("Flights","From")).click()
        time.sleep(5)
        self.driver.find_elements_by_css_selector(ConfigReader.test_homeloc("Flights","Dcity")).send_keys("Delhi")
