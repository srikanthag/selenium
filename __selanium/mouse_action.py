from selenium import webdriver
from time import sleep
import re
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(r"C:\Users\srikanth\Desktop\IT\Python\python_practice\_selenium\chromedriver.exe")
driver.get("https://www.monsterindia.com/")

'''move_to_element'''
driver.find_element_by_xpath("//button[@class='No thanks']").click()
action = ActionChains(driver)
profile = driver.find_element_by_xpath("//a[text()='Job search']")
action.move_to_element(profile).perform()

'''double_click'''



