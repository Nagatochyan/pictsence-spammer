from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
choice = input("Insert 1:" )
if choice =="1":
    doko=input("部屋のURL")
    web=doko
    chrome = webdriver.Chrome(executable_path='Your Path')
    chrome.get(web)
    choicee = input("入室できたら1をおす" )
    if choicee =="1":
        ka = int(input("何回送りますか？"))
        for i in range(ka):
            mail = chrome.find_element_by_xpath ('//*[@id="chatText"]')
            mail.send_keys("Nagato")
            element = chrome.find_element_by_xpath ('//*[@id="chatSubmitButton"]')
            element.submit()
