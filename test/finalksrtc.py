import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains 
import time 

parentDir = "C:/Users/kanith1234/Downloads/redbus"
driver = webdriver.Chrome()
driver.get("https://www.redbus.in/online-booking/rtc-directory")

driver.implicitly_wait(5)
print("Opened => ", driver.title)

#Find the element having government of south
south = driver.find_element(By.XPATH, '/html/body/div[1]/div/article[2]/div/div/ul[3]')
print("Selecting the direction => South ................")

ksrtc_kerala = driver.find_element(By.XPATH,'/html/body/div[1]/div/article[2]/div/div/ul[3]/li[4]')
print("Clicking =>",ksrtc_kerala.text)
ksrtc_foldername = ksrtc_kerala.text
ActionChains(driver).move_to_element(south).click(ksrtc_kerala).perform()

path = os.path.join(parentDir,ksrtc_foldername) 
os.makedirs(path)

# Handling the errors with folder creation
try: 
    os.makedirs(path, exist_ok = True) 
    print("Directory '%s' created successfully" % ksrtc_foldername) 
except OSError as error: 
    print("Directory '%s' can not be created" % ksrtc_foldername) 


ksrtc_kerala_routes = driver.find_elements(By.CLASS_NAME, "route_link")
print(len(ksrtc_kerala_routes)," routes found in ",ksrtc_foldername)
len_ksrtc_kerala = len(ksrtc_kerala_routes)

inner = f"C:/Users/kanith1234/Downloads/redbus/{ksrtc_foldername}"    


for i in range(2, len_ksrtc_kerala+2):
        kkRoute = driver.find_element(By.XPATH, f"//body/div[1]/div/div[4]/div[{i}]/div[1]/a")
        folderName =  kkRoute.text
