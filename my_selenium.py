import csv

import time

import dsp_utils as util
import register_objects as ro
import add_target as at
import object_to_pa as pa
from selenium import webdriver


driver = webdriver.Chrome()
driver.get('http://10.1.1.225/dsp/Virtual.aspx')
driver.implicitly_wait(50)

user = driver.find_element_by_id('username')
pw = driver.find_element_by_id('passwd')
login_btn = driver.find_element_by_id('login-button')
user.send_keys('administrator')
pw.send_keys('Br3wst3r')
login_btn.click()

util.navigate_to_migrate(driver)
ro.navigate_to_add_page(driver)

with open('objects.csv', 'r') as f:
    print('Starting Adding Objects######################')
    lines = csv.reader(f, delimiter='\t')
    for line in lines:
        time.sleep(0.5)
        ro.add_one_object(driver, line)
    print('Finishing Adding Obejcts#####################')
time.sleep(1)
util.wait_xpath(driver, '//*[@id="loadSiteBar"]/div/span[1]').click()
util.navigate_to_migrate(driver)
util.select_pa(driver, 'PTP')
with open('objects.csv', 'r') as f:
    lines = csv.reader(f, delimiter='\t')
    for line in lines:
        pa.start_add(driver, line)

driver.close()

