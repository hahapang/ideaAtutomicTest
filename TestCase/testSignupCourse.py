import unittest
from Action.userLogin import Action
from Webpage.CourseDetail import CourseDetail
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait

class TestSignup(unittest.TestCase):
    def test_signup_course(self):
        home_page = Action.user_login_home(1)

        signup_course = CourseDetail.jump_to_me(home_page)
        assert "自动化测试课程标题" in signup_course.web_driver.title

        studyBtn = signup_course.find_by_className (value='studyBtn')

        studyBtn.click()

        # WebDriverWait(driver, 10).until(EC.title_contains("元素"))

        signBtn = signup_course.find_by_className(value='mic-btn')
        signBtn.click()

        signup_course.close()

