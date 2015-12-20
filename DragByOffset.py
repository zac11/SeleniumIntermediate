__author__ = 'rahul'
 
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
 
 
 
class DragTest(unittest.TestCase):
 
    def setUp(self):
 
        self.driver = webdriver.Firefox()
 
    def test_dragelement(self):
 
        driver = self.driver
        driver.maximize_window()
        driver.get('http://jqueryui.com/draggable/')
 
 
        driver.switch_to.frame(0)
 
        source1 = driver.find_element_by_id('draggable')
        action = ActionChains(driver)
 
        #move element by x,y coordinates on the screen
        action.drag_and_drop_by_offset(source1, 100, 100).perform()
 
 
    def tearDown(self):
        self.driver.quit()
 
if __name__ == '__main__':
    unittest.main()
