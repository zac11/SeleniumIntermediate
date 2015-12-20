from selenium import webdriver
import unittest, time
import xlrd
 
class moduleName(unittest.TestCase):
      def setUp(self):
          self.driver = webdriver.Firefox()
 
 
      def test_Login(self):
          driver=self.driver
          driver.get(_url_of_the_webpage)
          driver.maximize_window()
           
           
          wb=xlrd.open_workbook('_location_of_the_file')
          sheetname = wb.sheet_names()
          
          #Read for XLSX Sheet names
          sh1 = wb.sheet_by_index(0)
 
          i=0
          while (i<2):
                rownum=(i)
                rows = sh1.row_values(rownum)
                element = driver.find_element_by_id("gbqfq")
                driver.find_element_by_id("gbqfq").send_keys(rows[0])
                element.submit()
                time.sleep(3)
                print "The keyword [" + rows[0] + "] is searched"
                driver.back()
                time.sleep(3)
                i=i+1
 
      def tearDown(self):
           self.driver.quit()
  
if __name__ == "__main__":
unittest.main()
