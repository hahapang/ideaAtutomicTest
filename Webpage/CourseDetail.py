from Webpage.Base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from TestCase.testCourse import TestCourse

class CourseDetail(Base):
    path = TestCourse().test_create_course()

    PATH = '/course/'+path

    def is_me(self):
        return WebDriverWait(self.web_driver, 10).until(
            expected_conditions.title_is('自动化测试课程标题')
        )
