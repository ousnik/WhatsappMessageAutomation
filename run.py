from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait     
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from dbmanagement import getLists

day = input('Day: ')
linkMsg = input('Meeting Link: ')
idMsg= "Meeting ID: "+input('Meeting ID: ')
pMsg= "Password: "+input('Password: ')
timeMsg="Please Join at "

nameList,timeList,waList = getLists(day)

driver = webdriver.Chrome("chromedriver.exe")
driver.get('https://web.whatsapp.com/')
wait = WebDriverWait(driver, 600) 

input('Scan QR code and press Enter Key!')

searchPointer = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]")

checkList=[]

print("\nTo be sent to: ")
print(nameList)

print("\nSending now: ")
for i in range(len(waList)):
    # myMsg=timeMsg+timeList[i]+" today."
    myMsg=timeMsg+"your respective time today."
    print("\n"+nameList[i]+': ',end='')
    for waName in waList[i]:
        if waName in checkList:
            print("--"+waName,end='-- | ')
            continue
        print(waName,end=' | ')
        checkList.append(waName)
        searchPointer.send_keys(waName)
        x_arg="//span[@title='{}']".format(waName)
        user = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
        user.click()
        msg_box =  driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
        msg_box.send_keys("Piu Ma'am is inviting you to attend your class today.")
        msg_box.send_keys(Keys.SHIFT, Keys.ENTER)                                                                           
        msg_box.send_keys(Keys.SHIFT, Keys.ENTER)
        msg_box.send_keys("Join Zoom Meeting")
        msg_box.send_keys(Keys.SHIFT, Keys.ENTER)
        msg_box.send_keys(linkMsg)
        msg_box.send_keys(Keys.SHIFT, Keys.ENTER)
        msg_box.send_keys(Keys.SHIFT, Keys.ENTER)
        msg_box.send_keys(idMsg)
        msg_box.send_keys(Keys.SHIFT, Keys.ENTER)
        msg_box.send_keys(pMsg)
        msg_box.send_keys(Keys.SHIFT, Keys.ENTER)
        msg_box.send_keys(Keys.SHIFT, Keys.ENTER)
        # msg_box.send_keys(myMsg)
        msg_box.send_keys(Keys.ENTER)
        msg_box.clear()
        searchPointer.clear()