'''WAIT FOR VISIBILITY OF “FIRSTNAME” TEXTBOX IN DEMO HTML PAGE'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep

driver = webdriver.Chrome(r"C:\Users\srikanth\Desktop\Selenium_project\chromedriver_win32\chromedriver.exe")
driver.get("file:///C:/Users/srikanth/Downloads/demo.html")

# wait = WebDriverWait(driver, 10)
# wait.until(expected_conditions.visibility_of_element_located(('name', 'fname')))
# driver.find_element_by_name('fname').send_keys('srikanth')

'''WAIT FOR PROGRESS BAR TO COMPLETE 100% IN DEMO HTML PAGE'''
# driver.find_element_by_xpath("//button[text()='Double-click me']").click
# wait = WebDriverWait(driver, timeout=10)
# wait.until(expected_conditions.visibility_of_element_located(('xpath', '//div[text()=100%')))
# print('done')

