from Webpage.Base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Config.config import asset_info
from time import sleep
title_input_path = "//*[@placeholder='请输入作品题目（允许2-20个字）']"
author_input_path = "//*[@placeholder='请输入作者姓名']"
#cover_input_path = "//*[@id='root']/div[1]/div/div[1]/section[1]/form/div[4]/div[2]/div/div/label/input"
cover_input_path = "//*[@id='root']/div[2]/div/div[1]/section[1]/form/div[4]/div[2]/div/div/label/input"
#cover_class_name = "micFileUp mic-new-fileUp"
#text_input_name = "m-editor-container"
text_input_path = "//*[@id='root']/div[2]/div/div[1]/section[2]/div[2]/form/div/div[2]/div/div/div[2]/div"

class CreateAsset(Base):
    PATH = '/userCenter/my/asset/post'
    def is_me(self):
        return WebDriverWait(self.web_driver, 10).until(
            expected_conditions.title_is('创建作品')
        )
    def input_asset_info(self, index):
        asset = asset_info[index]

        title_Input = self.find_by_xpath(xpath=title_input_path)
        title_Input.send_keys(asset["title"])

        author_Input = self.find_by_xpath(xpath=author_input_path)
        author_Input.send_keys(asset["author_name"])

        cover_Input = self.find_by_xpath(xpath=cover_input_path)
        cover_Input.send_keys(asset["cover"])
        sleep(3)

        text_Input = self.find_by_xpath(xpath=text_input_path)
        #text_Input.send_keys(asset["description"])
        text_Input.send_keys("rfghyuioy67u8i9o")


        sleep(4)