# modules include many functions to interact with the file system.
# The selenium.webdriver module provides all the WebDriver implementations
# The By class is used to locate elements within a document.
# Action chains are a sequence of actions that are performed in a specific order on a web page to test for a specific outcome. 
# These actions can be anything like clicking on an element, keypress, entering text, scrolling, dragging and dropping an object, etc.
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains 
import time 

parentDir = "C:/Users/kanith1234/Downloads/redbus"
# the instance of Chrome WebDriver is created.
driver = webdriver.Chrome()
# Opening the data
# The driver.get method will navigate to a page given by the URL.
driver.get("https://www.redbus.in/online-booking/rtc-directory") #------------------> the rtc -directory page will be opened


# waiting 5 seconds for the page to load
driver.implicitly_wait(5)
print("Opened => ", driver.title)

#Find the element having government of south
south = driver.find_element(By.XPATH, '/html/body/div[1]/div/article[2]/div/div/ul[3]')
print("Selecting the direction => South ................")


#locating element having the link to wbengal transports
ksrtc_kerala = driver.find_element(By.XPATH,'/html/body/div[1]/div/article[2]/div/div/ul[3]/li[4]')
print("Clicking =>",ksrtc_kerala.text)
ksrtc_foldername = ksrtc_kerala.text
#using actionchains, moving to east element and clicking on wbengal bus section
ActionChains(driver).move_to_element(south).click(ksrtc_kerala).perform()



# Create a folder in the parent directory with bengal govn bus dept name
path = os.path.join(parentDir,ksrtc_foldername) 
os.makedirs(path)

# Handling the errors with folder creation
try: 
    os.makedirs(path, exist_ok = True) 
    print("Directory '%s' created successfully" % ksrtc_foldername) 
except OSError as error: 
    print("Directory '%s' can not be created" % ksrtc_foldername) 

#Find available bus routes in KSRTC Kerala
ksrtc_kerala_routes = driver.find_elements(By.CLASS_NAME, "route_link")
print(len(ksrtc_kerala_routes)," routes found in ",ksrtc_foldername)
# result will be zero routes found in KSRTC (_Kerala)
len_ksrtc_kerala = len(ksrtc_kerala_routes)

# Defining a path for each bus route in the bengal bus routes
inner = f"C:/Users/kanith1234/Downloads/redbus/{ksrtc_foldername}"    

#Loop through all the bus routes in KSRTC (Kerala)
for i in range(2, len_ksrtc_kerala+2):
    #Find the route link
    # /html/body/div[1]/div/div[4]/div[2]/div[1]/a
    # /html/body/div[1]/div/div[4]/div[2]
    # /html/body/div[1]/div/div[4]/div[3]
    # /html/body/div[1]/div/div[4]/div[4]
    # /html/body/div[1]/div/div[4]/div[5]
    # /html/body/div[1]/div/div[4]/div[6]
    # /html/body/div[1]/div/div[4]/div[7]
    # /html/body/div[1]/div/div[4]/div[8]
    # /html/body/div[1]/div/div[4]/div[9]
    # /html/body/div[1]/div/div[4]/div[10]
    # /html/body/div[1]/div/div[4]/div[11]

    kkRoute = driver.find_element(By.XPATH, f"//body/div[1]/div/div[4]/div[{i}]/div[1]/a")
    folderName =  kkRoute.text #Save current route link text in a variable
   
    # ActionChains(driver).click(kkRoute).perform()
    # print("Opened => ", driver.title)   
    # driver.implicitly_wait(4) #Wait 4 sec to load the page

    # path= os.path.join(inner,folderName)  #Create a folder for each bus route
    # os.makedirs(path)

    print(folderName)
   

    # want to get the route_details

#     #Taking the number of different govt state bus services on current route
#     Routes = driver.find_elements(By.CLASS_NAME, "route_details")
#     total = len(Routes)
#     print(total, "=> Availaible Routes ",folderName," route")
#     if(total!=0):
#         #looping inside those govt routes
#         # /html/body/div[1]/div/div[4]/div[2]/div[1]/a
#         # /html/body/section/div[2]/div[4]/div/div[2]/div/div[2]/div[2]/div[2]
#         # /html/body/section/div[2]/div[4]/div/div[2]/div/div[2]/div[2]/div[3]
#         for bus in range(1, total+1):
#             moveTo = driver.find_element(By.XPATH, f"//section/div[2]/div[4]/div/div[2]/div/div[2]/div[2]/div[{bus}]")
#             clickBtn = driver.find_element(By.XPATH, f"//section/div[2]/div[4]/div/div[2]/div/div[2]/div[2]/div[{bus}]/div/div[2]/div/div[4]/div[2]")
#             ActionChains(driver).move_to_element(moveTo).click(clickBtn).perform()

#             #TO scroll bottom down, in order to get the dynamic content which only appear while scrolling down
#             bottomDiv = driver.find_element(By.ID,"seo-data")
#             ActionChains(driver).scroll_to_element(bottomDiv).perform()

#             #find the ul list having the respected govt's bus details
#             ulData = driver.find_element(By.XPATH, f"//section/div[2]/div[4]/div/div[2]/div/div[2]/div[2]/div[{bus}]/div[3]/ul")
#             textsdets = ulData.get_attribute('outerHTML')

#             #Creating a file for each bus dept, and writing the total bus details into a created file
#             with open(f"{bengalFoldername}/{folderName}/govroute_{bus}.html","w", encoding='utf-8') as f:
#                 f.write(textsdets)
            
#             #Scroll to top for clicking hide all button
#             ActionChains(driver).scroll_to_element(moveTo).perform()
#             ActionChains(driver).move_to_element(moveTo).click(clickBtn).perform()
        
#     else:
#         print(total," bus routes in ",folderName)


# driver.get("https://www.redbus.in/online-booking/west-bengal-transport-corporation")

# driver.close()






























