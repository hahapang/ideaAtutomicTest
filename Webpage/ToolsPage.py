from Webpage.Base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class KitPage(Base):
    PATH = '/kit'

    def is_me(self):
        return WebDriverWait(self.web_driver, 10).until(
            expected_conditions.title_is('套件')
        )

class ModulePage(Base):
    PATH = '/module'

    def is_me(self):
        return WebDriverWait(self.web_driver, 10).until(
            expected_conditions.title_is('模块')
        )

class SoftListPage(Base):
    PATH = '/softList'

    def is_me(self):
        return WebDriverWait(self.web_driver, 10).until(
            expected_conditions.title_is('软件下载')
        )
