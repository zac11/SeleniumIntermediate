__author__ = 'rahul'
 
import unittest
from selenium import webdriver
 
class JSPrompt(unittest.TestCase):
 
    def setUp(self):
        self.driver = webdriver.Firefox()
 
    def test_JSPrompt(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('http://the-internet.herokuapp.com/javascript_alerts?__s=xg1k6kuwg5ks2nkp3wfa&utm_campaign=elemental-selenium-ruby&utm_medium=email&utm_source=51-javascript-alerts')
 
       #get the third button by using it's xpath and click on it
        btn3 = driver.find_element_by_xpath("//*[@id='content']/div/ul/li[3]/button")
        btn3.click()
   
       #switch to the alert
        jsprompt= driver.switch_to.alert
 
       #send custom text to the prompt using send_keys( ) method
        jsprompt.send_keys('Rahul')
 
        #accept the alert
        jsprompt.accept()
 
        #assert that the result returned is what we expected
        textReturned = driver.find_element_by_id('result')
 
        print(textReturned.text)
 
        self.assertTrue(textReturned.text,'You entered: Rahul')
 
    def tearDown(self):
        self.driver.quit()
 
 
if __name__ == '__main__':
    unittest.main()
