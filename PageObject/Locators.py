class Locators:
    msg_list_item = "//span[text()='JK-JIOENG']/ancestor::mws-conversation-list-item[@class='ng-star-inserted']/a"
    msg_list_item_desc = "//mws-conversation-list-item[@class='ng-star-inserted']/a/div[contains(@class,'text-content')]/div[@class='snippet-text ng-star-inserted']"
    msg_content = "//*[@class='text-msg-content'])[10]/div"
    msg_top_timestamp = "//div[@class='content']//mws-relative-timestamp[@class='tombstone-timestamp ng-star-inserted']"
    # msg_info points to latest msg. So occurs once each page.
    msg_info = "//div[@class='content']//div[@class='msg-info']"
    msg_info_time = "//div[@class='content']//div[@class='msg-info']/mws-relative-timestamp"
