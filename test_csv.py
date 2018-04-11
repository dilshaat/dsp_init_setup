import time
from selenium import webdriver

driver = webdriver.Firefox()

driver.get('http://10.1.1.225/dsp/Virtual.aspx')

user = driver.find_element_by_id('username')
pw = driver.find_element_by_id('passwd')
login_btn = driver.find_element_by_id('login-button')
user.send_keys('administrator')
pw.send_keys('Br3wst3r')
login_btn.click()
time.sleep(1)
driver.find_element_by_xpath('//*[text()="dspMigrate"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[contains(text(), "PTP")]/parent::td/following-sibling::td[2]').click()
time.sleep(1)    
driver.back()
time.sleep(1)
driver.find_element_by_xpath('//*[contains(text(), "SD")]/parent::td/following-sibling::td[2]').click()
