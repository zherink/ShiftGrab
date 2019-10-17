#keep a list of used keys in a file so that they are not attempted to be put back in
#stop scraper whenever a used key is found
#only go to rewards page if new key was found
#https://shift.gearboxsoftware.com/rewards
#will probably need to sign in

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import re

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://twitter.com/dgShiftCodes")

tweets = driver.find_elements_by_class_name("TweetTextSize")
for tweet in tweets:
    text = tweet.text
    reg = re.search(r"((\w-?){5}){5}",text)
    if reg is None:
        continue
    print(reg.group())

