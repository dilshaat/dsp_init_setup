import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

dspMigrate_xpath = '//span[text()="dspMigrate"]'

def wait_xpath(driver, xpath):
    return  WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    
def build_xpath_objects(identifier):
    return '//table[@class="detailtable"]/tbody//td[text()="{0}"]/following-sibling::td[1]/input'.format(identifier)

def fill_objects_details(driver, name, description, comment):
    # Building the XPATH for Objects Details
    # Using HTML Table structure for Objects Form in DSP
    # Name         [________]
    # Description  [________]
    # Comment      [________]
    xpath_name = build_xpath_objects('Name') 
    xpath_description = build_xpath_objects('Description')
    xpath_comment = build_xpath_objects('Comment')
    # Filling the Form above in DSP Vertical View
    wait_xpath(driver, xpath_name).send_keys(name)
    wait_xpath(driver, xpath_description).send_keys(description)
    wait_xpath(driver, xpath_comment).send_keys(comment)

def navigate_to_migrate(driver):
    wait_xpath(driver, dspMigrate_xpath).click()

### SELECTING DSP Process Area
#   First build the XPATH for Process Area
#   Then click the objects Icon
def build_pa_xpath(identifier):
    return "//*[starts-with(text(), '{0}')]/parent::td/following-sibling::td[@positionindex='5']".format(identifier)


def select_pa(driver, pa):
    wait_xpath(driver, build_pa_xpath(pa)).click()
