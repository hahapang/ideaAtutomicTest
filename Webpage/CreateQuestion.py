#coding:utf-8
from Webpage.Base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Config.config import question_info
from selenium import webdriver
from time import sleep

class CreateQuestion(Base):
    PATH = '/question/post'

    def is_me(self):

        return WebDriverWait(self.web_driver, 10).until(
            expected_conditions.title_is('提问问题')
        )

    @staticmethod
    def openCreateQuestion():

        return webdriver.get("http://idea-lab-client.office.microduino.cn/question/post")

    def input_question_info(self, index):
        question = question_info[index]

        self.sendKey_by_xpath("//input[@placeholder= '请输入问题标题']", value= question["title"])

        #self.sendKey_by_xpath("//*[@id='root']/div[2]/div/div[2]/form/div[2]/div[2]/div/div/div",value=question["description"])

        self.sendKey_by_name("m-editor-container", value= question["description"])
        #self.sendKey_by_name("m-editor-container", value='Some Q')
        sleep(5)
