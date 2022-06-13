from selenium import webdriver
import unittest
from webdriver_manager.chrome import ChromeDriverManager

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('Listy', self.browser.title)
        self.fail('zakonczenie testu')

if __name__ == '__main__':
    unittest.main(warnings='ignore')


# import time
#
# from selenium import webdriver
#


#
# driver = webdriver.Chrome(ChromeDriverManager().install())  # Optional argument, if not specified will search path.
#
# driver.get('http://www.google.com/');
#
# time.sleep(5) # Let the user actually see something!
#
# search_box = driver.find_element_by_name('q')
#
# search_box.send_keys('ChromeDriver')
#
# search_box.submit()
#
# time.sleep(5) # Let the user actually see something!
#
# driver.quit()