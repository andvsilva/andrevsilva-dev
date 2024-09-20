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
from selenium.webdriver.common.keys import Keys

from tqdm import tqdm

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
    ntime = random.randint(100,250)
    print(f"long sleep for {ntime}s...")
    time.sleep(ntime)

def short_sleep():
    ntime = random.randint(20,30)
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

def wdriver():

    # Specify the path to your WebDriver executable
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)

    # URL of the webpage you want to open
    target_url = "https://www.google.com/"

     # Navigate to the specified URL
    driver.get(target_url)
    short_sleep()

    return driver


def search(driver):
    search = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
    search.send_keys("andrevsilva.com")
    search.send_keys(Keys.ENTER)

def click_link(driver):
    xpath = '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/span/a/h3'
    driver.find_element(By.XPATH, f'{xpath}').click()
    

if __name__ == "__main__":
    
    while True:   
        driver = wdriver()

        search(driver)

        click_link(driver)

        long_sleep()

#while True:

    # Get start time 
    #start_time = time.time()

    #location = random.choice(locations)

    #print(f" >>> Connecting to {location}")
    #os.system(f"windscribe connect {location}")

    #lpapers = []

