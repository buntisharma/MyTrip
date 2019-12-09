from selenium.webdriver import Chrome
from Library import ConfigReader
from Base.InitiateDriver import test_BrowserDriver
# from ScreenShot import Shot
import configparser
from Pages import Flights
import pytest
import unittest

from Pages.Flights import test_bookair
#from ScreenShot.teakS import test_Screenshot
from ScreenShot.teakS import take_page_sreenshot


class test_Air():
    def __init__(self,driver=None):
        self.driver=driver
    def test_byair(self):
        bd = test_BrowserDriver()
        self.driver = bd.test_startBrowser()
        log = test_bookair
        self.driver = log.test_searchflights(self)
        # self.log.test_searchjob(driver)
        #return self.test_byair()

look=test_Air()
look.test_byair()

