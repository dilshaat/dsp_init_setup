import csv
import dsp_utils as util
import register_objects as ro
import add_target as at
from selenium import webdriver


driver = webdriver.Chrome()
driver.get('http://10.1.1.225/dsp/Virtual.aspx')
driver.implicitly_wait(10)

user = driver.find_element_by_id('username')
pw = driver.find_element_by_id('passwd')
login_btn = driver.find_element_by_id('login-button')
user.send_keys('administrator')
pw.send_keys('Br3wst3r')
login_btn.click()

util.navigate_to_migrate(driver)
# For Object association to Process Area only
util.select_pa(driver,'PTP')

util.wait_xpath(driver, at.build_xpath_targets_btn('EAM-CONF')).click()

with open('targets.csv', 'r') as f:
    lines = csv.reader(f, delimiter='\t')
    for i in lines:
        at.add_targets_to_object(i[1], i[3], i[4], i[2], driver)

