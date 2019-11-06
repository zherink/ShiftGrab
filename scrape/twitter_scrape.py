#logger?

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import re
import os
from twilio.rest import Client
import time

twilio_client = Client(os.getenv('TWILIO_SID'), os.getenv('TWILIO_AUTH'))

chrome_options = Options()
arg_user_data = 'user-data-dir=' + os.getcwd() + '/profile'
chrome_options.add_argument(arg_user_data)
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)

driver.get('https://twitter.com/dgShiftCodes')
try:
    f = open('used_keys.txt', 'r')
except:
    open('used_keys.txt', 'a').close()
    f = open('used_keys.txt', 'r')

tweets = None
i = 0
while tweets == None:
    try:
        tweets = driver.find_elements_by_class_name('TweetTextSize')
    except:
        time.sleep(1)
        i = i + 1
        if i == 20:
            driver.quit()
            print('driver could not get tweets')
            exit()

keys = []
used_keys = f.read()
f.close()
for tweet in tweets:
    i = 0
    text = None
    while text == None:
        try:
            text = tweet.text
        except:
            time.sleep(1)
            i = i + 1
            if i == 20:
                driver.quit()
                print('text cannot be found in tweets')
                exit()
    
    reg = re.search(r'((\w-?){5}){5}',text)
    if reg is None:
        continue
    if reg.group() in used_keys:
        continue
    keys.append(reg.group())

if len(keys) == 0:
    print('No new keys :(')
    driver.quit()
    exit()

print('ALL KEYS: ')
print(keys)

f = open('used_keys.txt', 'a')
print('trying keys....')

driver.get('https://shift.gearboxsoftware.com/rewards')
if driver.current_url == 'https://shift.gearboxsoftware.com/rewards':
    try:
        # driver.find_element_by_xpath('/html/body/div[2]/nav/div/div[2]/ul[2]/li[2]/a').click()
        driver.find_element_by_link_text('Sign Out').click()
    except:
        print('could not see sign out button')

i = 0
while driver.current_url != 'https://shift.gearboxsoftware.com/rewards':
    if i == 10:
        print('Could not sign in')
        driver.quit()
        exit()
    print('Must sign in')
    try:
        driver.find_element_by_id('user_email').send_keys(os.getenv('SHIFT_EMAIL'))
        driver.find_element_by_id('user_password').send_keys(os.getenv('SHIFT_PASS'))
        driver.find_element_by_name('commit').click()
    except:
        print('Attempt: ' + str(i))
    i = i + 1
    driver.get('https://shift.gearboxsoftware.com/rewards')

for key in keys:
    if driver.current_url != 'https://shift.gearboxsoftware.com/rewards':
        driver.get('https://shift.gearboxsoftware.com/rewards')
    try:
        driver.find_element_by_id('shift_code_input').send_keys(key)
        driver.find_element_by_id('shift_code_check').click()
        driver.find_element_by_class_name('redeem_button').click()
        twilio_client.messages.create(to=os.getenv('TWILIO_TO'), from_=os.getenv('TWILIO_FROM'), body='SHiFT Code Redeemed')
        print('redeemed for Zach: ' + key)
    except:
        print('could not process key: ' + key)
    finally:
        driver.find_element_by_id('shift_code_input').clear()
    f.write(key + '\n')

print('Trying keys for Grayson')
try:
    driver.get('https://shift.gearboxsoftware.com/rewards')
    if driver.current_url == 'https://shift.gearboxsoftware.com/rewards':
        driver.find_element_by_link_text('Sign Out').click()
    
    i = 0
    while driver.current_url != 'https://shift.gearboxsoftware.com/rewards':
        if i == 10:
            print('Could not sign in')
            driver.quit()
            exit()
        print('Must sign in')
        try:
            driver.find_element_by_id('user_email').send_keys(os.getenv('SHIFT_GRAYSON_EMAIL'))
            driver.find_element_by_id('user_password').send_keys(os.getenv('SHIFT_GRAYSON_PASS'))
            driver.find_element_by_name('commit').click()
        except:
            print('Attempt: ' + str(i))
        i = i + 1
        driver.get('https://shift.gearboxsoftware.com/rewards')


    for key in keys:
        if driver.current_url != 'https://shift.gearboxsoftware.com/rewards':
            driver.get('https://shift.gearboxsoftware.com/rewards')
        try:
            driver.find_element_by_id('shift_code_input').send_keys(key)
            driver.find_element_by_id('shift_code_check').click()
            driver.find_element_by_class_name('redeem_button').click()
            twilio_client.messages.create(to=os.getenv('TWILIO_GRAYSON'), from_=os.getenv('TWILIO_FROM'), body='SHiFT Code Redeemed')
            print('redeemed for Grayson: ' + key)
        except:
            print('could not process key: ' + key)
        finally:
            driver.find_element_by_id('shift_code_input').clear()
except Exception as e:
    print('could not process keys for Grayson')
    print(e)

print('Trying keys for Josh')
try:
    driver.get('https://shift.gearboxsoftware.com/rewards')
    if driver.current_url == 'https://shift.gearboxsoftware.com/rewards':
        driver.find_element_by_link_text('Sign Out').click()
    
    i = 0
    while driver.current_url != 'https://shift.gearboxsoftware.com/rewards':
        if i == 10:
            print('Could not sign in')
            driver.quit()
            exit()
        print('Must sign in')
        try:
            driver.find_element_by_id('user_email').send_keys(os.getenv('SHIFT_JOSH_EMAIL'))
            driver.find_element_by_id('user_password').send_keys(os.getenv('SHIFT_JOSH_PASS'))
            driver.find_element_by_name('commit').click()
        except:
            print('Attempt: ' + str(i))
            print(driver.current_url)
        i = i + 1
        driver.get('https://shift.gearboxsoftware.com/rewards')


    for key in keys:
        if driver.current_url != 'https://shift.gearboxsoftware.com/rewards':
            driver.get('https://shift.gearboxsoftware.com/rewards')
        try:
            driver.find_element_by_id('shift_code_input').send_keys(key)
            driver.find_element_by_id('shift_code_check').click()
            driver.find_element_by_class_name('redeem_button').click()
            # twilio_client.messages.create(to=os.getenv('TWILIO_GRAYSON'), from_=os.getenv('TWILIO_FROM'), body='SHiFT Code Redeemed')
            print('redeemed for Josh: ' + key)
        except:
            print('could not process key: ' + key)
        finally:
            driver.find_element_by_id('shift_code_input').clear()
except Exception as e:
    print('could not process keys for Josh')
    print(e)
driver.quit()
