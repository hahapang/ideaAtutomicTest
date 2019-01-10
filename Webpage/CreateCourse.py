from Webpage.Base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Config.config import course_info
from time import sleep

class CreateCourse(Base):
    PATH = '/userCenter/my/course/post'

    def is_me(self):
        return WebDriverWait(self.web_driver, 10).until(
            expected_conditions.title_is('创建课程')
        )

    # 添加课程基本信息
    def input_course_info(self, index):
        course = course_info[index]

        self.sendKey_by_xpath(xpath="//*[@placeholder='请输入作品题目（允许2-20个字）']",value=(course["title"]))

        self.sendKey_by_xpath(xpath="//*[@placeholder='请输入作者姓名']",value=(course["author_name"]))

        self.sendKey_by_xpath(xpath="//*[@placeholder='课程简介']", value=(course["subscription"]))

        self.sendKey_by_xpath(xpath="//*[@id='root']/div[1]/div/div[1]/section[1]/form/div[5]/div[2]/div/div/label/input", value=(course["cover"]))

        self.sendKey_by_xpath(xpath="//*[@aria-label='rdw-editor']", value=(course["description"]))

        element = self.web_driver.find_element_by_xpath(xpath="//*[@id='root']/div[1]/div/div[1]/section[1]/form/div[6]/div[2]/span/span[1]")
        element.click()

    #引用课时
    def add_class_info(self):

        #页面滚动至底
        self.scroll_to_bottom()

        element = self.web_driver.find_element_by_xpath(xpath="//input[@value='引用课时']")
        element.click()

        self.find_by_className("modalForm")
        self.sendKey_by_xpath(xpath="//input[@placeholder='搜索课时']",value="第一课")

        sleep(1)
        classSelection = self.find_by_className("refClassCard")
        classSelection.click()

        sleep(1)
        element = self.web_driver.find_element_by_xpath(xpath="//input[@value= '确认']")
        element.click()
