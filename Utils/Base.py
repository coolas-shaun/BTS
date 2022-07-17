import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#TODO: refer - lambda test website

chrome_options = Options()
chrome_options.add_argument("user-data-dir=C:\\Users\\shaun\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3")
# chrome_options.add_argument('--profile-directory=default')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.implicitly_wait(10)
driver.maximize_window()
time.sleep(3)
driver.get("https://messages.google.com/web/conversations")

# $
print(driver.title)
ele1 = driver.find_element(By.XPATH,"//span[text()='JK-JIOENG']/ancestor::mws-conversation-list-item[@class='ng-star-inserted']/a")
# # ele1 = driver.find_element_by_xpath(
# #     "//span[text()='TM-WOWSKN']/ancestor::mws-conversation-list-item[@class='ng-star-inserted']/a")
#
# # time.sleep(10)
ele1.click()
time.sleep(3)
msg = driver.find_element(By.XPATH,"(//*[@class='text-msg-content'])[10]/div")
print(msg.text)

driver.close()

