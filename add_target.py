import time

from dsp_utils import wait_xpath


current_obj = 'EAM-CONF'
save_btn = ''
priority_input_xpath = '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[2]/div[2]/div/div[2]/table/tbody/tr[1]/td[5]/input'
ttName_input_xpath = '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[2]/div[2]/div/div[2]/table/tbody/tr[1]/td[6]/input'
desc_input_xpath = '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[2]/div[2]/div/div[2]/table/tbody/tr[1]/td[7]/input'

def build_xpath_targets_btn(identifier):
    return '//div[contains(text(), "{}")]/parent::td/following-sibling::td[2]'.format(identifier)

def has_targets(driver):
    global save_btn
    try:
        save_btn = wait_xpath(driver, '//*[@id="Save"]/div/span')
        return True
    except:
        return False

def add_targets_to_object(obj_name, priority, ttName, Desc, driver):
    global current_obj
    if current_obj == obj_name:
        time.sleep(1)
        fill_target_details(priority, ttName, Desc, driver)
    else:
        # wait_xpath(driver, '//*[@id="Cancel"]/div/span').click()
        time.sleep(2)
        current_obj = obj_name
        # if has_targets(driver):
        driver.back()
        wait_xpath(driver, build_xpath_targets_btn(current_obj)).click()
        time.sleep(1)
        fill_target_details(priority, ttName, Desc, driver)


def fill_target_details(priority, ttName, Desc, driver):
    wait_xpath(driver, priority_input_xpath).send_keys(priority)
    wait_xpath(driver, ttName_input_xpath).send_keys(ttName)
    wait_xpath(driver, desc_input_xpath).send_keys(Desc)
    wait_xpath(driver, '//*[@id="Save"]/div/span').click()
