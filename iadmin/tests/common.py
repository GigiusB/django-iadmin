from django.conf import settings
from django.test import LiveServerTestCase
import selenium.webdriver.firefox.webdriver
import selenium.webdriver.chrome.webdriver


class SeleniumTestCase(LiveServerTestCase):
    urls = 'iadmin.tests.urls'
    fixtures = ['test.json',]
#    driverClass = selenium.webdriver.firefox.webdriver.WebDriver

    @property
    def base_url(self):
        return self.live_server_url

    @classmethod
    def setUpClass(cls):
        cls.driver = cls.driverClass()
        super(SeleniumTestCase, cls).setUpClass()
        settings.LANGUAGE_CODE = 'en-US'

    @classmethod
    def tearDownClass(cls):
        super(SeleniumTestCase, cls).tearDownClass()
        cls.driver.quit()

    def setUp(self):
        super(SeleniumTestCase, self).setUp()


    def go(self, url):
        self.driver.get('%s%s' % (self.live_server_url, url))

    def login(self):
        u = '%s%s' % (self.live_server_url, '/admin/')
        self.driver.get(u)
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys('sax')
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys('123')
        self.driver.find_element_by_xpath('//input[@type="submit"]').click()
        self.assertEqual("Site administration | Django site admin", self.driver.title)


class FirefoxDriverMixin(object):
    driverClass = selenium.webdriver.firefox.webdriver.WebDriver

class ChromeDriverMixin(object):
    driverClass = selenium.webdriver.chrome.webdriver.WebDriver

class FireFoxLiveTest(FirefoxDriverMixin, SeleniumTestCase):
    pass