import time
import wait_utils as wu
import register_objects as ro
import object_to_pa as pa
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



driver = webdriver.Chrome()
driver.get('http://10.1.1.225/dsp/Virtual.aspx')
driver.implicitly_wait(20)

user = driver.find_element_by_id('username')
pw = driver.find_element_by_id('passwd')
login_btn = driver.find_element_by_id('login-button')
user.send_keys('administrator')
pw.send_keys('Br3wst3r')
login_btn.click()

pa.navigate_dspMigrate(driver)
pa.select_pa(driver,'PTP')

lst = [
['EAM-FLOC', 'Fucntional Location', '100'],
['EAM-BOM', 'Bill of Material', '200'],
['EAM-EQ', 'EQUIPMENT', '300'],
['EAM-COMM', 'COMMON', '400'],
['EAM-CLASS', 'CLASS', '500']	
]

for item in lst:
    pa.add_object_pa(driver, item)
driver.close()