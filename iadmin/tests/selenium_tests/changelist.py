from django.core.urlresolvers import reverse
from iadmin.tests.selenium_tests.common import FireFoxLiveTest, ChromeDriverMixin

class CellFilterFireFox(FireFoxLiveTest):

    def setUp(self):
        super(CellFilterFireFox, self).setUp()
        self.url = reverse("iadmin:auth_user_changelist")

    def _test_menu_open(self):
        self.login()
        self.go( self.url )
        self.driver.find_elements_by_class_name('iadmin-cell-menu-button')[0].click()

    def test_equals_to(self):
        self.login()
        self.driver.implicitly_wait(10)
        self.go( self.url )
        # get the menu container
        container = self.driver.find_elements_by_class_name('iadmin-cell-menu-container')[0]
        # click the button...
        container.find_elements_by_class_name('iadmin-cell-menu-button')[0].click()
        # and click the 'Equals to' menu item
        container.find_element_by_link_text('Equals to').click()

        # collects all the rows
        tbody = self.driver.find_element_by_css_selector('#result_list tbody')
        rows = tbody.find_elements_by_class_name('action-checkbox')
        self.assertEquals(len(rows), 1)

    def test_not_equals_to(self):
        self.login()
        self.driver.implicitly_wait(10)
        self.go(self.url )
        # get the menu container
        container = self.driver.find_elements_by_class_name('iadmin-cell-menu-container')[0]

        # click the button...
        container.find_elements_by_class_name('iadmin-cell-menu-button')[0].click()
        # and click the 'Equals to' menu item
        container.find_element_by_link_text('Not equals to').click()

        # collects all the rows
        tbody = self.driver.find_element_by_css_selector('#result_list tbody')
        rows = tbody.find_elements_by_class_name('action-checkbox')
        self.assertEquals(len(rows), 11)
#        self.driver.save_screenshot()

    def test_equals_to_bool(self):
        self.login()
        self.driver.implicitly_wait(10)
        self.go(self.url)
        # get the menu container
        container = self.driver.find_elements_by_class_name('iadmin-cell-menu-container')[2]
        # click the button...
        container.find_elements_by_class_name('iadmin-cell-menu-button')[0].click()
        # and click the 'Equals to' menu item
        container.find_element_by_link_text('Yes').click()

        # collects all the rows
        tbody = self.driver.find_element_by_css_selector('#result_list tbody')
        rows = tbody.find_elements_by_class_name('action-checkbox')
        self.assertEquals(len(rows), 1)

    def test_not_equals_to_bool(self):
        self.login()
        self.driver.implicitly_wait(10)
        self.go(self.url)
        # get the menu container
        container = self.driver.find_elements_by_class_name('iadmin-cell-menu-container')[2]
        # click the button...
        container.find_elements_by_class_name('iadmin-cell-menu-button')[0].click()
        # and click the 'Equals to' menu item
        container.find_element_by_link_text('No').click()

        # collects all the rows
        tbody = self.driver.find_element_by_css_selector('#result_list tbody')
        rows = tbody.find_elements_by_class_name('action-checkbox')
        self.assertEquals(len(rows), 11)

class CellFilterChrome(ChromeDriverMixin, CellFilterFireFox):
    pass
