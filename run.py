from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait     
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By 
from dbmanagement import getNameList

driver = webdriver.Chrome("chromedriver.exe")

driver.get('https://web.whatsapp.com/')

wait = WebDriverWait(driver, 600) 

nameList = getNameList()
# nameList = ['Beta']
msg = "https://us04web.zoom.us/j/73219365942?pwd=akxXcW1PZmZIbzdaWE90Y1F1RzVtQT09 Meeting ID: 732 1936 5942 Password: 123456"

input('Scan QR code and press Enter Key!')

searchPointer = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]")
for name in nameList:
    searchPointer.send_keys(name)
    x_arg="//span[@title='{}']".format(name)
    user = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    user.click()
    msg_box =  driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
    msg_box.send_keys(msg)
    msg_box.clear()
    # searchPointer.clear()
    x_arg2="//*[@id='main']/footer/div[1]/div[3]/button"
    button = wait.until(EC.presence_of_element_located((By.XPATH, x_arg2)))
    # button =  driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button")
    button.click()

