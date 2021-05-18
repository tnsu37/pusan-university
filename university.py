import time
import selenium
from selenium import webdriver

people_list_string=input(">> : ")
people_list=people_list_string.split(",")

URL = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query='
driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get(url=URL)

for number in people_list:
    search_box=driver.find_element_by_name("query")
    search_box.send_keys(number)

    search_btn=driver.find_element_by_class_name("bt_search")
    search_btn.click()

    map_name=driver.find_element_by_class_name("title").text
    rate=driver.find_element_by_class_name("text").text

    print(map_name+" - "+rate)

    time.sleep(3)
    search_box = driver.find_element_by_name("query")
    search_box.clear()

time.sleep(3)

driver.close()