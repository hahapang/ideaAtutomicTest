import unittest
from Webpage.QuestionPage import QuestionPage
from Action.userLogin import Action
from Webpage.CreateQuestion import CreateQuestion
from time import sleep

class TestQuestion(unittest.TestCase):
        # def test_questionpage(self):
        #     question_page = QuestionPage()
        #     try:
        #         question_page.open()
        #         assert "提问问题" in question_page.web_driver.title
        #
        #     finally:
        #         question_page.close()

    def test_question(self):
        home_page = Action.user_login_home(0)

        create_question = CreateQuestion.jump_to_me(home_page)
        assert "" in create_question.web_driver.title

        create_question.input_question_info(0)
        sleep(2)

        btn = create_question.find_by_xpath("//input[@value = '提交问题']")
        btn.click()







