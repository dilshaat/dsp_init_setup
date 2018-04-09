import time
from wait_utils import wait_xpath
from wait_utils import fill_objects_details
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


dspMigrate_xpath = '//span[text()="dspMigrate"]'
elements_xpath = '//div[@id="navigationview"]//span[text()="Elements"]'
objects_xpath = '//div[@id="navigationview"]//span[text()="Object"]'
add_btn_xpath = '//div[@titletext="Objects"]//span[text()="Add"]'
save_btn_xpath = '//div[@id="detailview"]//div[@class="gridActionToolbar"]//span[text()="Save"]'
back_btn_xpath = '/html/body/div[1]/div[2]/div[4]/div/div[1]/div[1]/span[1]'
edit_btn_xpath = '//span[text()="Edit"]'

def navigate_to_add_page(driver):
    wait_xpath(driver, dspMigrate_xpath).click()
    wait_xpath(driver, elements_xpath).click()
    wait_xpath(driver, objects_xpath).click()
    
def try_click_add(driver):
    attemtp = 0
    res = False
    while attemtp < 3:
        try:
            wait_xpath(driver, add_btn_xpath).click()
            res = True
            print('worked!!!!!!!!!!!!!!!!!!!!!!')
            break
        except StaleElementReferenceException:
            print('Exeption Occurred!!!!!!!!!!!!!!!!!')
        attemtp += 1
    return res


def add_one_object(driver, object_line):
    try_click_add(driver) 
    save = wait_xpath(driver, save_btn_xpath)
    fill_objects_details(driver, object_line[0], object_line[1], object_line[2])
    save.click()
    edit = wait_xpath(driver, edit_btn_xpath)
    while not (edit.is_displayed() and edit.is_enabled):
        print('waiting...for Edit button')
    wait_xpath(driver, back_btn_xpath).click()