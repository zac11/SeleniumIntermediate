__author__ = 'rahul'
 
import unittest
from selenium import webdriver
 
 
class JSAlertConfirm(unittest.TestCase):
 
    def setUp(self):
        self.driver = webdriver.Firefox()
    def test_JSAlertConfirm(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('http://the-internet.herokuapp.com/javascript_alerts?__s=xg1k6kuwg5ks2nkp3wfa&utm_campaign=elemental-selenium-ruby&utm_medium=email&utm_source=51-javascript-alerts')
      
        #get the second button by xpath and click on it
        btn2 = driver.find_element_by_xpath("//*[@id='content']/div/ul/li[2]/button")
 
        btn2.click()
 
        #switch to the alert
        jsalert= driver.switch_to.alert
         
        #accept the alert
        jsalert.accept()
   
       #get the resultant text and assert if it is same as we want
        textReturned = driver.find_element_by_id('result')
 
        print(textReturned.text)
 
        self.assertTrue(textReturned.text, 'You Clicked: Ok')
 
 
        #refresh the webpage
        driver.refresh()
  
        #get the button again and click on it
        btn2 = driver.find_element_by_xpath("//*[@id='content']/div/ul/li[2]/button")
 
        btn2.click()
 
       #switch to alert
        jsalert = driver.switch_to.alert
 
       #to cancel the alert, we need to use dismiss( ) method
        jsalert.dismiss()
 
       #get the resultant text and assert if it is same as we expect.
        textReturned2 = driver.find_element_by_id('result')
 
        print(textReturned2.text)
 
        self.assertTrue(textReturned2.text,'You Clicked: Cancel')
 
 
 
 
    def tearDown(self):
        self.driver.quit()
 
 
if __name__ == '__main__':
    unittest.main()
