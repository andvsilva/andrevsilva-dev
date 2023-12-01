import os
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# free account
locations=['US', 'CA', 'UK', 'HK', 'FR', 
           'DE', 'NL', 'CH', 'NO', 'RO', 
           'TR'
           ]

# PRO
"""
locations = ['US', 'CA', 'UK', 'HK', 'FR', 'DE', 
             'NL', 'CH', 'NO', 'RO', 'TR', 'IT', 
             'ES', 'SE', 'IE', 'DK', 'PL', 'AT', 
             'CZ', 'HU', 'FI', 'BG', 'BE', 'LV', 
             'LT', 'PT', 'SK', 'MD', 'HR', 'GR', 
             'EE', 'AL', 'RS', 'BA', 'CY', 'MK', 
             'IS', 'UA', 'IN', 'RU', 'AZ', 'IL', 
             'ZA', 'AR', 'BR', 'CO', 'MX', 'PA', 
             'PE', 'CL', 'AU', 'NZ', 'JP', 'SG', 
             'KR', 'TW', 'MY', 'VN', 'TH', 'ID', 
             'PH', 'KH', 'EC', 'KE', 'GH', 'FA'
            ]
"""

def long_sleep():
    ntime = random.randint(60,90)
    print(f"long sleep for {ntime}s...")
    time.sleep(ntime)

def short_sleep():
    ntime = random.randint(20,35)
    print(f"short sleep for {ntime}s...")

def scroldownpage(driver):
    height = driver.execute_script("return document.body.scrollHeight")
    
    for scrol in range(100,height,100):
        delay = random.randint(1,4)
        print('scroldown...')
        driver.execute_script(f"window.scrollTo(0,{scrol})")

        time.sleep(delay)

def wdriver(target_url, xpath):

    # Specify the path to your WebDriver executable
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)

    # Navigate to the specified URL
    driver.get(target_url)

    # Wait for the page to load (you can adjust the wait time based on your needs)
    time.sleep(5)

    # Locate the link by its text
    # Click on the link
    driver.find_element(By.XPATH, f'{xpath}').click()
    print(f"Clicked on the link")
    time.sleep(5)

    scroldownpage(driver)

    short_sleep()

    # Close the browser window
    driver.quit()

while True:
    location = random.choice(locations)

    print(f" >>> Connecting to {location}")
    os.system(f"windscribe connect {location}")

    # URL of the webpage you want to open
    target_url = "http://andrevsilva.com"

    # element xpaths
    xpaths =['//*[@id="top"]/div[2]/div[1]/div/article[1]/div[2]/div[1]/h2/a',
             '//*[@id="top"]/div[2]/div[1]/div/article[2]/div[2]/div[1]/h2/a',
             '//*[@id="top"]/div[2]/div[1]/div/article[3]/div[2]/div[1]/h2/a',
             '//*[@id="top"]/div[2]/div[1]/div/article[4]/div[2]/div[1]/h2/a',
             '//*[@id="top"]/div[2]/div[1]/div/article[5]/div[2]/div[1]/h2/a',
             '//*[@id="top"]/div[2]/div[1]/div/article[6]/div[2]/div[1]/h2/a',
             '//*[@id="top"]/div[2]/div[1]/div/article[7]/div[2]/div[1]/h2/a',
             '//*[@id="top"]/div[2]/div[1]/div/article[8]/div[2]/div[1]/h2/a',
             '//*[@id="top"]/div[2]/div[1]/div/article[10]/div[2]/div[1]/h2/a',
             '//*[@id="top"]/div[2]/div[1]/div/article[11]/div[2]/div[1]/h2/a'
           ]

    for xpath in xpaths:
        wdriver(target_url, xpath)
        
    long_sleep()


    #processRunning_id = driver.service.process.pid
    
    #long_sleep()
    #os.system(f"kill {processRunning_id}")
