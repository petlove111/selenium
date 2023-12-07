
#driver2=webdriver.Chrome()

#driver1.get("https://www.naver.com")
#driver2.get("https://comic.naver.com/index")

#driver1.back()
#driver1.forward()
#driver1.close()

#driver1.maximize_window()
#driver1.minimize_window()
#driver1.set_window_size(500,300)
#driver1.set_window_position(100,100)

#u=["https://www.naver.com","https://www.youtube.com","https://comic.naver.com"]
#d=[]
#for i in range(len(u)):
#    driver=webdriver.Chrome()
#    d.append(driver)
#   d[i].get(u[i])
#import time

#driver1.set_window_size(200,300)
#driver1.set_window_position(0,0)
#for i in range(4):
#   time.sleep(1)
#   driver1.set_window_position(i*100, i*100)

'''
from selenium import webdriver

w=1920/2
h=1080/2

pos=[(0,0),(w,0),(0,h),(w,h)]

d=[]

u=["https://www.naver.com","https://www.youtube.com","https://comic.naver.com","https://github.com"]

for i in range(len(u)):
    driver=webdriver.Chrome()
    d.append(driver)
    d[i].set_window_size(w,h)
    d[i].set_window_position(pos[i][0],pos[i][1])
    d[i].get(u[i])


'''
'''
#햄버거 아저씨 홈페이지 

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
serv=Service()
serv.creation_flags=CREATE_NO_WINDOW
driver=webdriver.Chrome(service=serv)

driver.get("https://sbasu.pythonanywhere.com/tastyFoodApp/")

p='//*[@id="homePageLinks"]/ul/li/a'
e=driver.find_element('xpath',p)
e.click()

import time
time.sleep(2)

p='//*[@id="id_firstName"]'
e=driver.find_element('xpath',p)
e.send_keys("Inseo")

p='//*[@id="id_lastName"]'
e=driver.find_element('xpath',p)
e.send_keys("Jang")

p='//*[@id="id_gender_1"]'
e=driver.find_element('xpath',p)
e.click()

p='//*[@id="id_username"]'
e=driver.find_element('xpath',p)
e.send_keys("petlove111")

p='//*[@id="id_password"]'
e=driver.find_element('xpath',p)
e.send_keys("dream5429!")

p='//*[@id="id_state"]'
e=driver.find_element('xpath',p)
e.click()

p='//*[@id="id_state"]/option[3]'
e=driver.find_element('xpath',p)
e.click()

p='//*[@id="id_fee"]'
e=driver.find_element('xpath',p)
e.click()

p='//*[@id="id_fee"]/option[4]'
e=driver.find_element('xpath',p)
e.click()

p='//*[@id="id_date"]'
e=driver.find_element('xpath',p)
e.send_keys("01/12/2012")

import time
time.sleep(2)

p='/html/body/form/div/input'
e=driver.find_element('xpath',p)
e.click()
'''
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
serv=Service()
serv.creation_flags=CREATE_NO_WINDOW
driver=webdriver.Chrome(service=serv)

driver.get("https://www.google.co.kr/?hl=ko")
p='//*[@id="APjFqb"]'
e=driver.find_element('xpath',p)
e.send_keys("연세초등학교")
'''

#유튜브
'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
serv=Service()
serv.creation_flags=CREATE_NO_WINDOW
driver=webdriver.Chrome(service=serv)

driver.get("https://www.youtube.com/")
p='//input[@id="search"]'
e=driver.find_element('xpath',p)
e.send_keys("세븐틴 음악의 신")

from selenium.webdriver.common.keys import Keys
e.send_keys(Keys.RETURN)

import time
time.sleep(3)

p='//a[@id="thumbnail"]'
elements=driver.find_elements('xpath',p)
print(elements[2].get_attribute('href'))
driver.get(elements[2].get_attribute('href'))

'''
#유튜브 검색
'''
query=["음악의 신 호시 직캠","손오공 호시 직캠","울고싶지 않아 호시 직캠"]

from selenium.webdriver.common.keys import Keys
import time

for i in range(3):
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from subprocess import CREATE_NO_WINDOW
    serv=Service()
    serv.creation_flags=CREATE_NO_WINDOW
    driver=webdriver.Chrome(service=serv)

    driver.get("https://www.youtube.com/")
    p='//input[@id="search"]'
    e=driver.find_element('xpath',p)
    e.send_keys(query[i])
    time.sleep(3)
    e.send_keys(Keys.RETURN)
    time.sleep(3)

'''
#텍스트 저장
'''
text='안녕하세요'
file=open('테스트.txt','w')
file.write(text)
file.close()
'''

#학교종이

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
serv=Service()
serv.creation_flags=CREATE_NO_WINDOW
driver=webdriver.Chrome(service=serv)

driver.get("https://v4.schoolbell-e.com/ko/gate/home?return_uri=https:%2F%2Fschoolbell-e.com%2Fko%2Fmain%2F")
p='/html/body/schoolbelle-root/div/app-gate/app-gate-home/div[1]/div[3]/div[1]/div/button[1]'
e=driver.find_element('xpath',p)
e.click()

import time
time.sleep(3)

p='/html/body/schoolbelle-root/div/app-gate/app-gate-login/div/div[1]/div/form/div[1]/div[1]/phone-number-input/div/input'
e=driver.find_element('xpath',p)
e.send_keys("01089074060")

p='/html/body/schoolbelle-root/div/app-gate/app-gate-login/div/div[1]/div/form/div[2]/div/input'
e=driver.find_element('xpath',p)
e.send_keys("dream2005")

p='/html/body/schoolbelle-root/div/app-gate/app-gate-login/div/div[1]/div/form/div[3]/button'
e=driver.find_element('xpath',p)
e.click()

time.sleep(2)

p='/html/body/app-root/app-main/div[1]/app-main-home/div[2]/div[1]/div[1]/app-my-group-slides/div/ngu-carousel/div/div[1]/div/ngu-tile[1]/div/div[1]/div/div[1]'
e=driver.find_element('xpath',p)
e.click()

time.sleep(2)



info=[ ]
for i in range(10):
    temp=[ ]
    p=f'/html/body/app-root/app-main/div[1]/app-main-group/div[2]/div[1]/div[2]/div/app-group-board/div/div/virtual-scroller/div[2]/div/div[{i+1}]/div/app-letter-item-short/div/div/div/div[2]/extended-letter-metadata/p/span'
    e=driver.find_element('xpath',p)
    temp.append(e.text)
    p=f'/html/body/app-root/app-main/div[1]/app-main-group/div[2]/div[1]/div[2]/div/app-group-board/div/div/virtual-scroller/div[2]/div/div[{i+1}]/div/app-letter-item-short/div/div/div/div[2]/h6/app-translation-viewer/span'
    e=driver.find_element('xpath',p)
    temp.append(e.text)
    info.append(temp)

file=open('테스트.txt','w')
for i in range(10):
    file.write(info[i][0].replace("발행","")+ ":"+ info[i][1]+"\n")
file.close()

'''
#네이버 뉴스기사

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
serv=Service()
serv.creation_flags=CREATE_NO_WINDOW
driver=webdriver.Chrome(service=serv)
import time

query=["세븐틴","호시","탕후루","마라탕"]

for i in range(len(query)):
    driver.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query="+query[i])
    time.sleep(3)
    driver.save_screenshot(query[i]+".jpg")
'''
