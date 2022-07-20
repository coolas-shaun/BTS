import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# TODO: refer - lambda test website

class WebDriverSetUp:
    def __init__(self, browser):
        self.browser = browser

    driver = None

    def driver_setup(self):
        if self.browser == "chrome":
            chrome_options = Options()
            chrome_options.add_argument(
                "user-data-dir=C:\\Users\\shaun\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3")
            WebDriverSetUp.driver = webdriver.Chrome(chrome_options=chrome_options)
            return WebDriverSetUp.driver


class Base:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.get(url)

    def click_element(self, locator):
        self.driver.find_element(By.XPATH, locator).click()
        time.sleep(3)

    def get_text_from_element(self, locator):
        return self.driver.find_element(By.XPATH, locator).text

    def browser_teardown(self):
        self.driver.close()
        self.driver.quit()

# $
# print(driver.title)
# ele1 = driver.find_element(By.XPATH,
#                            "//span[text()='JK-JIOENG']/ancestor::mws-conversation-list-item[@class='ng-star-inserted']/a")
# # ele1 = driver.find_element_by_xpath(
# #     "//span[text()='TM-WOWSKN']/ancestor::mws-conversation-list-item[@class='ng-star-inserted']/a")
#
# # time.sleep(10)
# ele1.click()
# time.sleep(3)
# msg = driver.find_element(By.XPATH, "(//*[@class='text-msg-content'])[10]/div")
# print(msg.text)

#driver.close()

#d
# d
