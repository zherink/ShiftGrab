#keep a list of used keys in a file so that they are not attempted to be put back in
#stop scraper whenever a used key is found
#only go to rewards page if new key was found
#will probably need to sign in
#logger?

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import re
import os
from twilio.rest import Client

twilio_client = Client(os.getenv('TWILIO_SID'), os.getenv('TWILIO_AUTH'))

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('https://twitter.com/dgShiftCodes')
try:
    f = open('used_keys.txt', 'r')
except:
    open('used_keys.txt', 'a').close()
    f = open('used_keys.txt', 'r')


tweets = driver.find_elements_by_class_name('TweetTextSize')
keys = []
used_keys = f.read()
f.close()
for tweet in tweets:
    text = tweet.text
    reg = re.search(r'((\w-?){5}){5}',text)
    if reg is None:
        continue
    if reg.group() in used_keys:
        break
    keys.append(reg.group())

if len(keys) == 0:
    driver.quit()
    exit()

print('ALL KEYS: ')
print(keys)

f = open('used_keys.txt', 'a')
message = []
print('sending keys....')
message.append(twilio_client.messages.create(
        to=os.getenv('TWILIO_TO'),
        from_=os.getenv('TWILIO_FROM'),
        body="NEW SHiFT Code key: " + ', '.join(keys)))
# driver.get('https://shift.gearboxsoftware.com/rewards')
for key in keys:
    f.write(key + '\n')

driver.quit()
