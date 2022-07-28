from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import random

os.system('color ' +random.choice(['a', 'b', 'c', 'd'])+ " & cls & title  Pictsence Spammer")
def pict():
    clear = lambda: os.system('cls')
    clear()
    print(f'[1]text spam')
    print(f'[2]mass make room') 
    print(f'[3]raid paintings')
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
    exit = input(f'エンターキーを押してください: ')
    exit = clear()
    exit = pict()

pict()
