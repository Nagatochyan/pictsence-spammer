 
    if choice =="2":
        
        doko=input("部屋のURL:")
        web=doko
        chrome = webdriver.Chrome(executable_path='chromedriver.exe')
        sasqw=webdriver.Chrome(executable_path='chromedriver.exe')
        def aa():
            chrome.get(web)
        def bb():
            sasqw.get(web)
        th1 = threading.Thread(target=aa)
        th2 = threading.Thread(target=bb)
        th1.start()
        th2.start()
        choicee = input("入室できたら1をおす" )
        if choicee =="1":
            Nagato=input("内容:")
            ka = int(input("何回送りますか？"))
            for i in range(ka):
                mail = chrome.find_element_by_xpath ('//*[@id="chatText"]')
                mail.send_keys(Nagato)
                element = chrome.find_element_by_xpath ('//*[@id="chatSubmitButton"]')
                element.submit()
        exit = input(f'エンターキーを押してください: ')
        exit = clear()
        exit = pict()
