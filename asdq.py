from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
choice = input("Insert 1 and press enter to start generating discord account!:" )
if choice =="1":
    web="https://pictsense.com/#!/1658918791374_56"
    chrome = webdriver.Chrome(executable_path='C:\\Users\\tamat\\3D Objects\\自作\\accountgen\\chromedriver.exe')
    chrome.get(web)
    choicee = input("Insert 1 and press enter to start generating discord account!:" )
    if choicee =="1":
        ka = int(input("何回送りますか？"))
        for i in range(ka):
            mail = chrome.find_element_by_xpath ('//*[@id="chatText"]')
            mail.send_keys("Nagato")
            element = chrome.find_element_by_xpath ('//*[@id="chatSubmitButton"]')
            element.submit()
