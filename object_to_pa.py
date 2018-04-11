import time

from dsp_utils import wait_xpath
from dsp_utils import select_pa
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import StaleElementReferenceException

add_btn_xpath = '//*[@id="Add"]/div/span'
data_source_id_xpath = '/html/body/div[1]/div[2]/div[4]/div/div[2]/div[2]/table/tbody/tr[3]/td[2]/div/a/span'
current_pa = 'PTP'

def try_click_add(driver):
    attempt = 0
    res = False
    while attempt < 5:
        try:
            time.sleep(0.5)
            wait_xpath(driver, add_btn_xpath).click()
            time.sleep(0.5)
            res = True
            print('worked!!!!!!!!!!!!!!!!!!!!!!')
            break
        except StaleElementReferenceException:
            print('Exeption Occurred!!!!!!!!!!!!!!!!!')
        attempt += 1
    return res


def add_object_pa(driver, line_object):
    print('***processing => ', line_object)
    try_click_add(driver)
    wait_xpath(driver, '//*[text()="[Choose one]"]').click()
    obj = '{} - {}'.format(line_object[0], line_object[1])
    print('inserting obj is: ', obj)
    obj_list = driver.find_elements_by_xpath('//span[@class="select2-match"]/parent::div')
    for o in obj_list:
        if o.text == obj:
            print('clicking...')
            o.click()
            print('clicked....!')
            break
    # wait_xpath(driver, '//*[@id="select2-drop"]/div[1]/input').send_keys(obj)
    # object_element = wait_xpath(driver, '//ul//div[@class="select2-result-label"]/span')
    # ActionChains(driver).move_to_element(object_element).click().perform()
    priority_element = wait_xpath(driver, '/html/body/div[1]/div[2]/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/table/tbody/tr[1]/td[5]/input')
    priority_element.send_keys(line_object[0])
    comment_element = wait_xpath(driver, '/html/body/div[1]/div[2]/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/table/tbody/tr[2]/td/input')
    comment_element.send_keys(line_object[2])
    time.sleep(0.5)
    wait_xpath(driver, '//*[@id="Save"]/div/span').click()
    data_source_id = wait_xpath(driver, data_source_id_xpath).text
    print(data_source_id)
    wait_xpath(driver, '//*[text()="[Choose one]"]').click()
    insert_box = wait_xpath(driver, '//*[@id="select2-drop"]/div[1]/input')
    time.sleep(0.5)
    ActionChains(driver).move_to_element(insert_box).send_keys(data_source_id).send_keys(Keys.ENTER).perform()
    wait_xpath(driver, '/html/body/div[1]/div[2]/div[4]/div/div[1]/div[2]/div[1]/div').click()

def start_add(driver, line):
    global current_pa
    if current_pa == line[4]:
        add_object_pa(driver, line)
    else:
        time.sleep(1)
        current_pa = line[4]
        driver.back()
        time.sleep(0.5)
        print(current_pa)
        time.sleep(4)
        driver.find_element_by_xpath('//*[contains(text(), "{0}")]/parent::td/following-sibling::td[2]'.format(current_pa)).click()
        # select_pa(driver, line)
        # WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), {0})]')))
        add_object_pa(driver, line)
