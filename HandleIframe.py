__author__ = 'rahul'
 
import unittest
from selenium import webdriver
 
 
class Iframe(unittest.TestCase):
 
    def setUp(self):
        self.driver = webdriver.Firefox()
 
    def test_Iframe(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('http://www.toolsqa.com/iframe-practice-page/')
 
        iframe1 = driver.find_element_by_id('IF1')
        driver.switch_to.frame(iframe1)
 
        driver.find_element_by_name('email').send_keys('xyz')
 
        driver.switch_to.default_content()
 
        list = driver.find_elements_by_tag_name('iframe')
 
        print(len(list))
 
    def tearDown(self):
        self.driver.quit()
 
 
if __name__ == '__main__':
    unittest.main()
