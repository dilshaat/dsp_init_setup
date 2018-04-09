from wait_utils import wait_xpath
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import StaleElementReferenceException

dspMigrate_xpath = '//span[text()="dspMigrate"]'
add_btn_xpath = '//*[@id="Add"]/div/span'
data_source_id_xpath = '/html/body/div[1]/div[2]/div[4]/div/div[2]/div[2]/table/tbody/tr[3]/td[2]/div/a/span'

def build_pa_xpath(identifier):
    return "//*[starts-with(text(), '{0}')]/parent::td/following-sibling::td[@positionindex='5']".format(identifier)

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

def navigate_dspMigrate(driver):
    wait_xpath(driver, dspMigrate_xpath).click()

def select_pa(driver, pa):
    wait_xpath(driver, build_pa_xpath(pa)).click()

def add_object_pa(driver, line_object):
    try_click_add(driver)
    wait_xpath(driver, '//*[text()="[Choose one]"]').click()
    wait_xpath(driver, '//*[@id="select2-drop"]/div[1]/input').send_keys(line_object[0])
    object_element = wait_xpath(driver, '//ul//div[@class="select2-result-label"]/span')
    ActionChains(driver).move_to_element(object_element).click().perform()
    priority_element = wait_xpath(driver, '/html/body/div[1]/div[2]/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/table/tbody/tr[1]/td[5]/input')
    priority_element.send_keys(line_object[2])
    comment_element = wait_xpath(driver, '/html/body/div[1]/div[2]/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/table/tbody/tr[2]/td/input')
    comment_element.send_keys(line_object[1])
    wait_xpath(driver, '//*[@id="Save"]/div/span').click()
    data_source_id = wait_xpath(driver, data_source_id_xpath).text
    print(data_source_id)
    wait_xpath(driver, '//*[text()="[Choose one]"]').click()
    insertbox = wait_xpath(driver, '//*[@id="select2-drop"]/div[1]/input')
    ActionChains(driver).move_to_element(insertbox).send_keys(data_source_id).send_keys(Keys.ENTER).perform()
    wait_xpath(driver, '/html/body/div[1]/div[2]/div[4]/div/div[1]/div[2]/div[1]/div').click()
