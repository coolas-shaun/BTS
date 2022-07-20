from PageObject.Locators import Locators
from Utils.Base import Base


class MainList:

    # def __init__(self, driver):
    #     # super().__init__(driver)
    #     self.driver = driver

    def get_message_content(self, Base):
        val = Base.get_text_from_element("(//*[@class='text-msg-content'])[10]/div")
        print(val)
