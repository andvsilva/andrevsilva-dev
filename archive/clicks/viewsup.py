import os
import snoop
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from tqdm import tqdm

# free account
"""
locations=['US', 'CA', 'UK', 'HK', 'FR', 
           'DE', 'NL', 'CH', 'NO', 'RO', 
           'TR'
           ]
"""

# PRO
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


def long_sleep():
    ntime = random.randint(10,25)
    print(f"long sleep for {ntime}s...")
    time.sleep(ntime)

def short_sleep():
    ntime = random.randint(3,6)
    print(f"short sleep for {ntime}s...")

def scroldownpage(driver):
    height = driver.execute_script("return document.body.scrollHeight")
    
    for scrol in range(100,height,300):
        delay = random.randint(1,4)
        driver.execute_script(f"window.scrollTo(0,{scrol})")

        time.sleep(delay)

def barprocess():
    ntime = random.randint(10,25)
    with tqdm(total=ntime, desc=f"Waiting...{ntime} s", bar_format="{l_bar}{bar} [ time left: {remaining} ]") as pbar:
        for i in range(ntime):
            time.sleep(1)
            pbar.update(1)

#@snoop
def wdriver(driver, xpath):

    # URL of the webpage you want to open
    target_url = "https://andsilvadrcc.medium.com/"

    # Navigate to the specified URL
    driver.get(target_url)

    driver.switch_to.new_window('tab')
    time.sleep(5)
    driver.get(target_url)

    driver.implicitly_wait(1)
    time.sleep(3)
    driver.find_element(By.XPATH, f'{xpath}').click()
    time.sleep(3)

    scroldownpage(driver)

    short_sleep()

while True:

    # Get start time 
    start_time = time.time()

    location = random.choice(locations)

    print(f" >>> Connecting to {location}")
    os.system(f"windscribe connect {location}")

    # Specify the path to your WebDriver executable
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)

    # element xpaths
    xpaths =['//*[@id="root"]/div/div[3]/div[2]/div/main/div/div[2]/div/div/article[8]/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div[1]/a/div[1]/h2',
             '//*[@id="root"]/div/div[3]/div[2]/div/main/div/div[2]/div/div/article[7]/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div[1]/a/div[1]/h2',
             '//*[@id="root"]/div/div[3]/div[2]/div/main/div/div[2]/div/div/article[6]/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div[1]/a/div[1]/h2',
             '//*[@id="root"]/div/div[3]/div[2]/div/main/div/div[2]/div/div/article[5]/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div[1]/a/div[1]/h2',
             '//*[@id="root"]/div/div[3]/div[2]/div/main/div/div[2]/div/div/article[4]/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div[1]/a/div[1]/h2',
             '//*[@id="root"]/div/div[3]/div[2]/div/main/div/div[2]/div/div/article[3]/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div[1]/a/div[1]/h2',
             '//*[@id="root"]/div/div[3]/div[2]/div/main/div/div[2]/div/div/article[2]/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div[1]/a/div[1]/h2',
             '//*[@id="root"]/div/div[3]/div[2]/div/main/div/div[2]/div/div/article[1]/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div[1]/a/div[1]/h2'
           ]

    for xpath in xpaths:
        wdriver(driver, xpath)
    
    # Close the browser window
    driver.quit()

    time_exec_min = round( (time.time() - start_time)/60, 4)
    
    print(f'time of execution: {time_exec_min} minutes')
        
    barprocess()