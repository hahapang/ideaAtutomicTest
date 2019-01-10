from Webpage.Base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Config.config import user_info


class LoginPage(Base):
    PATH = '/signin?redirectUri=/'

    def is_me(self):
        return WebDriverWait(self.web_driver, 10).until(
            expected_conditions.title_is('用户登录')
        )

    def input_login_info(self, index):
        user = user_info[index]

        userInput = self.web_driver.find_element_by_xpath(xpath="//*[@placeholder='邮箱地址或电话号码']")
        userInput.send_keys(user["user_name"])

        password = self.web_driver.find_element_by_xpath(xpath="//*[@placeholder='密码']")
        password.send_keys(user["user_password"])
