from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(r"C:\Users\srikanth\Desktop\Selenium_project\chromedriver_win32\chromedriver.exe")

driver.get("file:///C:/Users/srikanth/Downloads/demo.html")
# cars = driver.find_element_by_id("standard_cars")
# s = Select(cars)
# all_option = s.options

'''select by visible_text'''
# s.select_by_visible_text("Audi")
# sleep(1)
# s.select_by_visible_text("Toyota")
# sleep(1)

'''select by index'''
# s.select_by_index(4)
# sleep(1)
# s.select_by_index(6)
# sleep(1)

'''select by value'''
# s.select_by_value('jgr')
# sleep(1)
# s.select_by_value('lr')
# sleep(1)

'''option'''
# cars = driver.find_element_by_id("standard_cars")
# s = Select(cars)
# all_option = s.options
#
# for item in all_option:
#     print(item.text)
#     sleep(2)
# driver.close()

'''select last item'''
# cars = driver.find_element_by_id("standard_cars")
# s = Select(cars)
# all_option = s.options
#
# items = [item.text for item in all_option]
# s.select_by_visible_text(items[-1])

'''SELECTING EACH ITEM IN THE LIST BOX ONE BY ONE IN REVERSED ORDER'''
# cars = driver.find_element_by_id("standard_cars")
# s = Select(cars)
# all_option = s.options
#
# for item in all_option[::-1]:
#     print(item.text)
#     sleep(2)
# driver.close()

'''PRINT INDEX AT WHICH THE “Audi” IS PRESENT'''
# cars = driver.find_element_by_id("standard_cars")
# s = Select(cars)
# all_option = s.options
#
# items = [item.text for item in all_option]
# for index, item in enumerate(items):
#     if item == 'Audi':
#         print(f"{item} present in {index}")
#         sleep(2)
# driver.close()

'''first_selected_option'''
# cars = driver.find_element_by_id("standard_cars")
# s = Select(cars)
# s.select_by_visible_text('Audi')
# first_select_option = s.select_first_option.text

'''selecting multiple items in multi-select'''
# cars = driver.find_element_by_id("standard_cars")
# s = Select(cars)
# s.select_by_visible_text('Audi')
# sleep(1)
# s.select_by_visible_text('Toyota')
# sleep(1)
# s.select_by_visible_text('Mercedes')
# sleep(1)


'''is_multiple'''
# cars = driver.find_element_by_id("multiple_cars")
# s = Select(cars)
# print(s.is_multiple)
