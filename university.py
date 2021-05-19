import time
import selenium
from selenium import webdriver

people_list_string=input(">> : ")
people_list=people_list_string.split(",")

URL = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query='
driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get(url=URL)

y = []

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

    table = driver.find_elements_by_tag_name('table')
    tbody = table[0].find_elements_by_tag_name('tbody')
    tr_list = tbody[0].find_elements_by_tag_name('tr')
    for tr in tr_list:
        tr_td_list = tr.find_elements_by_tag_name('td')
        for td in tr_td_list:
            y.append(td.text)
y_1 = []
for i in y:
    y_1.append(i[0:4])
a=float(y_1[0])
b=float(y_1[1])
c=float(y_1[2])
y_2 = []
y_2.append(a)
y_2.append(b)
y_2.append(c)

import matplotlib.pyplot as plt
space=people_list
x=[1,2,3]
plt.rc('font', family='Malgun Gothic')
day=people_list
plt.bar(x,y_2,width=0.7)
plt.xticks(x,space)
plt.ylabel('인구 수')
plt.xlabel('지역')
plt.suptitle('지역 별 인구 수')
plt.show()




time.sleep(3)




driver.close()