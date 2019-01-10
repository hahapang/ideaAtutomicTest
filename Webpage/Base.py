from selenium import webdriver
from Config import config
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class Base(object):
    PATH = ''

    def __init__(self, browser='Chrome', web_driver=None):
        self.browser = browser
        browser = getattr(webdriver, browser)
        if web_driver is None:
            self.web_driver = browser('/Users/lijin/ideaLab_Automatic_Test/lib/chromedriver')
        else:
            self.web_driver = web_driver
        self.url = config.base_url + self.PATH

    @classmethod
    def jump_to_me(cls, context=None, args=''):
        if context is None:
            instance = cls()
        else:
            instance = cls(web_driver=context.web_driver, browser=context.browser)
        instance.open(args=args)
        return instance

    def is_me(self):
        raise NotImplementedError("Should have implemented this")

    def open(self, args =''):
        self.web_driver.get(self.url + args)
        if self.is_me() is not True:
            raise TimeoutError

    def close(self):
        self.web_driver.close()

    def find_by_xpath(self,xpath):
        return self.web_driver.find_element_by_xpath(xpath)

    def find_by_className(self,value):
        return self.web_driver.find_element_by_class_name(value)

    def navigate_by_xpath(self, to_web_page, xpath, method='click'):
        link_element = self.web_driver.find_element_by_xpath(xpath)
        to_do = getattr(link_element, method)
        to_do()
        instance = to_web_page(web_driver=self.web_driver, browser=self.browser)
        if instance.is_me() is not True:
            raise TimeoutError
        return instance

    def navigate_by_className(self, to_web_page,value, method='click'):
        link_element = self.web_driver.find_element_by_class_name(value)
        to_do = getattr(link_element,method)
        to_do()
        instance = to_web_page(web_driver= self.web_driver, browser= self.browser)
        if instance.is_me() is not True:
            raise TimeoutError
        return instance

    def navigate_by_link(self, to_web_page, value , method = 'click'):
        link_text  = self.web_driver.find_element_by_link_text(value)
        to_do = getattr(link_text, method)
        to_do()
        instance = to_web_page(web_driver = self.web_driver, browser= self.browser)
        if instance.is_me() is not True:
            raise TimeoutError
        return instance

    def sendKey_by_xpath(self, xpath, value):
        link_element = self.web_driver.find_element_by_xpath(xpath)
        return link_element.send_keys(value)

    def sendKey_by_name(self,key_name,value):
        class_name = self.web_driver.find_element_by_class_name(key_name)
        return class_name.send_keys(value)

    def scroll_to_bottom(self):
        return self.web_driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def scroll_to_top(self):
        return self.web_driver.execute_script("window.scrollTo(0, document.body.scrollTop=0)")

    def wait_until_show(self,element):
        WebDriverWait(webdriver,20,0.5).until(EC.presence_of_element_located(By.LINK_TEXT,element))
