from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def wait_xpath(driver, xpath):
    return  WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath))) 
    
def build_xpath_objects(identifier):
    return '//table[@class="detailtable"]/tbody//td[text()="{0}"]/following-sibling::td[1]/input'.format(identifier)

def fill_objects_details(driver, name, description, comment):
    xpath_name = build_xpath_objects('Name') 
    xpath_description = build_xpath_objects('Description')
    xpath_comment = build_xpath_objects('Comment')

    wait_xpath(driver, xpath_name).send_keys(name)
    wait_xpath(driver, xpath_description).send_keys(description)
    wait_xpath(driver, xpath_comment).send_keys(comment)

    



    
