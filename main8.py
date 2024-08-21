import os 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains        
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import csv

GenDir="C:/Users/kanith1234/Downloads/redbus/"
parentDir = "C:/Users/kanith1234/Downloads/redbus/bus"
# parentPathDir = "C:/Users/kanith1234/Downloads/redbus/pathes"



driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.redbus.in")  # Opening the redbus home page
driver.implicitly_wait(5)  # waiting 5 seconds for the page to load
# Finding the element having the view all button for navigating into government bus service page

governmentDepartments = driver.find_element(By.CLASS_NAME, "rtcHeadViewAll")
# Finding the path of the button for navigating into government bus service page
viewall = driver.find_element(By.XPATH, "//main/div[3]/div[3]/div[1]/div[2]/a")

# calling actionchains module to queue-up the click
ActionChains(driver).move_to_element(governmentDepartments).click(viewall).perform()

driver.switch_to.window(driver.window_handles[1])  #switch to the newly opened window
print("Switching to newly opened window => " + driver.title) 
driver.implicitly_wait(2) #wait 5 secs to load the content properly
#find the total number of different department regions

with open(f"{GenDir}/AllRoutes.csv","a") as f:
    writer = csv.writer(f)
    w=""
    writer.writerow(w)

#function to find private bus details
def scrape_quotes(deptDirectory, priPath):
    checkService = len(driver.find_elements(By.CLASS_NAME, "sort-results"))
    checkBroutes = len(driver.find_elements(By.CLASS_NAME,"bus-items"))
    if checkService!=0:
        if checkBroutes !=0:
            # Wait for the initial content to load
            WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.CLASS_NAME, "bus-items"))) 
            # Extract and print initial data
            initial_html = driver.page_source
            initial_soup = BeautifulSoup(initial_html, 'html.parser')
            initial_quotes = initial_soup.find_all('div', class_='clearfix bus-item')

            with open(f"{deptDirectory}/route.csv" ,"a", newline='') as file:
                writer = csv.writer(file)
                field = ["name","Route","Source", "Dest", "Duration","Starting time","Reach Time","Price","Seats","Rating"]
                writer.writerow(field)

            with open(f'AllRoutes.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                field = ["name","Route","Source", "Dest", "Duration","Starting time","Reach Time","Price","Seats","Rating"]
                writer.writerow(field)
            
            extract_and_print_quotes(initial_quotes,deptDirectory, priPath)
            extract_and_print_quotes_general(initial_quotes, deptDirectory, priPath)
            # Simulate scroll events to load additional content
            for scroll_count in range(15):  # Assuming there are 8 scroll events in total
                # Scroll down using JavaScript
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                # Wait for the dynamically loaded content to appear
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'bus-item')))
                # Extract and print the newly loaded quotes
                scroll_html = driver.page_source
                scroll_soup = BeautifulSoup(scroll_html, 'html.parser')
                scroll_quotes = scroll_soup.find_all('div', class_='clearfix bus-item')
                extract_and_print_quotes(scroll_quotes, deptDirectory, priPath)
                extract_and_print_quotes_general(scroll_quotes, deptDirectory, priPath)
            

#function to scrap private bus details
def extract_and_print_quotes(quotes, deptDirectory, priPath):
    with open('AllRoutes.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        for quote in quotes:
            name = quote.find('div', class_='travels').get_text(strip=True)
            source = quote.find('div', class_='dp-loc').get_text(strip=True)
            dest = quote.find('div', class_='bp-loc').get_text(strip=True)
            totTime = quote.find('div', class_='dur').get_text(strip=True)
            stime = quote.find('div', class_='dp-time').get_text(strip=True)
            rtime = quote.find('div',class_='bp-time').get_text(strip=True)
            price = quote.find('div', class_='fare').get_text(strip=True)
            seats = quote.find('div', class_='seat-left').get_text(strip=True)
            rating = quote.find('div', class_='column-six').get_text(strip=True)

            writer.writerow([f"{name}",f"{priPath}",f"{source}",f"{dest}",f"{totTime}",f"{stime}",f"{rtime}",f"{price}",f"{seats}",f"{rating}"])
    

#function to scrap private bus details
def extract_and_print_quotes_general(quotes, deptDirectory, priPath):
    with open(f"{deptDirectory}/route.csv" ,"a", newline='') as file:
        writer = csv.writer(file)
        for quote in quotes:
            name = quote.find('div', class_='travels').get_text(strip=True)
            source = quote.find('div', class_='dp-loc').get_text(strip=True)
            dest = quote.find('div', class_='bp-loc').get_text(strip=True)
            totTime = quote.find('div', class_='dur').get_text(strip=True)
            stime = quote.find('div', class_='dp-time').get_text(strip=True)
            rtime = quote.find('div',class_='bp-time').get_text(strip=True)
            price = quote.find('div', class_='fare').get_text(strip=True)
            seats = quote.find('div', class_='seat-left').get_text(strip=True)
            rating = quote.find('div', class_='column-six').get_text(strip=True)

            writer.writerow([f"{name}",f"{priPath}",f"{source}",f"{dest}",f"{totTime}",f"{stime}",f"{rtime}",f"{price}",f"{seats}",f"{rating}"])     


titles=[] #To store department's names
#find the total number of different deparments in each region
deptLinks = driver.find_elements(By.CLASS_NAME, "D113_link")  
for name in deptLinks:  #Save all the govt bus department names in a list
    titles.append(name.text)
    

for i in range(0, len(titles)):  #traverse the list for clicking each govt department
    clikables = driver.find_element(By.LINK_TEXT, f"{titles[i]}")
    ActionChains(driver).move_to_element(clikables).click(clikables).perform()
    driver.implicitly_wait(2)
    print("visited =>  ",titles[i])

    path = os.path.join(parentDir,f"{i}-{titles[i]}") 
    os.makedirs(path)
    deptDirectory = f"{parentDir}/{i}-{titles[i]}"

    totRoutes = driver.find_elements(By.CLASS_NAME, "route_link")
    if(len(totRoutes) == 0):
        #Go back to the deparment's home page
        print(f"===================================Skipped {titles[i]}===========================================\n")
        driver.find_element(By.XPATH, f"//body/div[1]/div/div[2]/div/ul/li[2]/a").click()

    else:
        #Check whether there is any paginations
        pagination=driver.find_elements(By.CLASS_NAME, "DC_117_pageTabs")
        print(len(pagination)," pages in ",titles[i])

        deptEachBusRoute=[]

        if len(pagination)>1:
            for page in range(1, len(pagination)+1):
                eachBusRoutes = driver.find_elements(By.CLASS_NAME, "route")
                for eachRoute in eachBusRoutes:
                    deptEachBusRoute.append(eachRoute.text)

                for eachRouteInBusRoute in deptEachBusRoute: 
                    enums=1
                    findRoute = driver.find_element(By.LINK_TEXT, f"{eachRouteInBusRoute}")
                    ActionChains(driver).move_to_element(findRoute).perform()
                    findRoute.send_keys(Keys.CONTROL + Keys.ENTER)
                    driver.switch_to.window(driver.window_handles[2])  #switch to the newly opened window
                    routeFolderName=f"{enums}-{eachRouteInBusRoute}"
                    scrape_quotes(deptDirectory,routeFolderName)
                    driver.close()
                    driver.switch_to.window(driver.window_handles[1])

                if(page<len(pagination)):
                    paginate=driver.find_element(By.XPATH, f"//body/div[1]/div/div[4]/div[12]/div[{page+1}]")
                    deptEachBusRoute.clear()
                    ActionChains(driver).move_to_element(paginate).click(paginate).perform()
                

        else:
            eachBusRoutes = driver.find_elements(By.CLASS_NAME, "route")   
            for eachRoute in eachBusRoutes:
                deptEachBusRoute.append(eachRoute.text)
            for eachRouteInBusRoute in deptEachBusRoute:
                enums=1
                url = driver.current_url
                findRoute = driver.find_element(By.LINK_TEXT, f"{eachRouteInBusRoute}")
                ActionChains(driver).move_to_element(findRoute).click(findRoute).perform()
                routeFolderName=f"{enums}-{eachRouteInBusRoute}"
                scrape_quotes(deptDirectory,routeFolderName)
                driver.get(url)
                

        print("==============================================================================\n")

        #Return Back to the home
        back=driver.find_element(By.XPATH, f"//body/div[1]/div/div[2]/div/ul/li[2]/a")
        ActionChains(driver).move_to_element(back).click(back).perform()

        
# time.sleep(3)
driver.close()


















