from Utils.Base import WebDriverSetUp, Base
from PageObject import Locators
from PageObject.Pages.MainList import MainList


def main():
    browser = "chrome"
    wd = WebDriverSetUp(browser)
    driver = wd.driver_setup()
    base = Base(driver)
    base.open_url("https://messages.google.com/web/conversations")
    base.click_element("//span[text()='JK-JIOENG']/ancestor::mws-conversation-list-item[@class='ng-star-inserted']/a")
    m = MainList()
    m.get_message_content(base)
    base.browser_teardown()


main()
