from selenium import webdriver
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
import json
import time
import math

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
caps = options.to_capabilities()
name_dfee = {}



driver = webdriver.Chrome(desired_capabilities = caps, executable_path='/Users/ryan/Desktop/FTDS/01Foundation/13-web-scraping-beautifulsoup/notebooks/chromedriver') # to open the chromebrowser 

driver.get("https://www.foodpanda.hk/city/hong-kong")

address_input = driver.find_element_by_id("delivery-information-postal-index")
address_input.send_keys("18 Whitfield Rd, Causeway Bay, Hong Kong")
driver.find_element_by_xpath("//*[@id='delivery-information-postal-index-form']/div[2]/button").click()
time.sleep(5)
last = driver.find_elements_by_xpath("//li[starts-with(@data-testid,'vendor')]")
last = last[-1]
print(last)
end = False
while end == False:   
    last.location_once_scrolled_into_view
    time.sleep(2)
    new = driver.find_elements_by_xpath("//li[starts-with(@data-testid,'vendor')]")[-1]
    if new == last:
        end = True
    else:
        last = new
print("success")
#find url
#url_list = driver.find_elements_by_xpath("//li[starts-with(@data-testid,'vendor')]/a")
# find figcation
figcaption = driver.find_elements_by_xpath("//figcaption[starts-with(@class,'vendor-info')]")

# find delivery fee
delivery_fee = driver.find_elements_by_xpath("//span[starts-with(@data-cy,'delivery-fee-active')]/span")

# find resto name
resto_name = driver.find_elements_by_xpath("//span[starts-with(@class,'name fn')]")

#print(len(delivery_fee))
#print(len(resto_name))
with open('/Users/ryan/Downloads/01Foundation/13-web-scraping-beautifulsoup/figcaption.txt','w') as f:
    for i in figcaption:
        f.write(i.text + "\n")
        
 #   for i in range(len(resto_name)):
  #      k = resto_name[i].text
   #     v = delivery_fee[i].text
    #    name_dfee[k]=v
    #name_dfee = json.dumps(name_dfee)
    #name_dfee_df=pd.DataFrame(name_dfee, header = False, index=False)
    #print(name_dfee_df)  
    #for i in url_list:
        #f.write(i.get_attribute('href')+"\n"+ d_fee.text)



#for d_fee in delivery_fee:       
    #print(d_fee.text)
#.get_attribute('href')
#action = ActionChains(driver)
#action.key_down(Keys.COMMAND).send_keys(Keys.ARROW_DOWN).key_up(Keys.COMMAND).perform()
#action.perform()


