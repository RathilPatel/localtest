from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os,  time ,requests
from browserstack.local import Local

USERNAME = os.environ['BROWSERSTACK_USERNAME']
BROWSERSTACK_ACCESS_KEY = os.environ['BROWSERSTACK_ACCESS_KEY']

desired_cap = {
 'browser': 'Chrome',
 'browser_version': '75.0',
 'os': 'Windows',
 'os_version': '7',
 'resolution': '1024x768',
 'browserstack.local' : 'true',   # LOCAl CAPABILITY
 'name': 'Python Local APIs',
 'build': 'Python Demo'
}


# 
try:
    driver = webdriver.Remote(command_executor='https://%s:%s@hub.browserstack.com/wd/hub' % (USERNAME, BROWSERSTACK_ACCESS_KEY),
    desired_capabilities=desired_cap)
    driver.get("localhost:45691/check")
    time.sleep(10)
    
    if "Up and running" in driver.page_source:
        requests.put('https://rathildemo:ysJ6rj6QKHcygJrtSjPu@api.browserstack.com/automate/sessions/'+driver.session_id+'.json', data={"status": "passed", "reason": ""})
    else:
        requests.put('https://rathildemo:ysJ6rj6QKHcygJrtSjPu@api.browserstack.com/automate/sessions/'+driver.session_id+'.json', data={"status": "failed", "reason": ""})
finally:
  
    driver.quit()


