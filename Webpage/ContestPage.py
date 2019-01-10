from Webpage.Base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class ContestPage(Base):
    PATH = '/contest'

    def is_me(self):
        return WebDriverWait(self.web_driver, 10).until(
            expected_conditions.title_is('赛事详情')
        )
