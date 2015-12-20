__author__ = 'rahul'
 
import unittest
from selenium import webdriver
 
 
class JSAlertCheck(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
 
    def test_JSAlert(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('http://the-internet.herokuapp.com/javascript_alerts?__s=xg1k6kuwg5ks2nkp3wfa&utm_campaign=elemental-selenium-ruby&utm_medium=email&utm_source=51-javascript-alerts')
 
       #this searches for for the first alert button and clicks on that
        btn1=driver.find_elements_by_css_selector('button')[1]
        btn1.click()
 
       #now we switch to alert
        popup = driver.switch_to.alert
 
       #use the accept() method to accept the alert
        popup.accept()
         
       #this gets the result text returned
        textreturned = driver.find_element_by_id('result')
 
        print(textreturned.text)
         
       #we assert if the text returned is what we wanted
        self.assertTrue(textreturned.text,"You Clicked: OK")
 
    def tearDown(self):
           self.driver.quit()
 
 
if __name__ == '__main__':
    unittest.main()
