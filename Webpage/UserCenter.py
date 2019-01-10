from Webpage.Base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class myAssetPage(Base):
    PATH = '/userCenter/my/asset'

    def is_me(self):
        return WebDriverWait(self.web_driver, 10).until(
            expected_conditions.title_is('我的作品')
        )

class myAssetCollection(Base):
    PATH = '/userCenter/collect/asset'

    def is_me(self):
        return WebDriverWait(self.web_driver, 10).until(
            expected_conditions.title_is('我收藏的作品列表')
        )

class myCourseCollection(Base):
    PATH = '/userCenter/collect/course'

    def is_me(self):
        return WebDriverWait(self.web_driver, 10).until(
            expected_conditions.title_is('我收藏的课程')
        )

class myCourse(Base):
    PATH = '/userCenter/my/course'

    def is_me(self):
        return WebDriverWait(self.web_driver, 10).until(
            expected_conditions.title_is('全部')
        )

class myClass(Base):
    PATH = '/userCenter/my/class'

    def is_me(self):
        return WebDriverWait(self.web_driver, 10).until(
            expected_conditions.title_is('我的课时')
        )

class myLearning(Base):
    PATH = '/userCenter/learning'

    def is_me(self):
        return WebDriverWait(self.web_driver, 10).until(
            expected_conditions.title_is('我学习的课程')
        )

class myHomework(Base):
    PATH = '/userCenter/my/homework'

    def is_me(self):
        return WebDriverWait(self.web_driver, 10).until(
            expected_conditions.title_is('我的作业')
        )

class myMessagePage(Base):
    PATH = '/userCenter/message'

    def is_me(self):
        return WebDriverWait(self.web_driver, 10).until(
            expected_conditions.title_is('互动信息')
        )

class myPassword(Base):
    PATH = '/userCenter/updatePassword'

    def is_me(self):
        return WebDriverWait(self.web_driver, 10).until(
            expected_conditions.title_is('修改密码')
        )

class myProfile(Base):
    PATH = '/userCenter/profile'

    def is_me(self):
        return WebDriverWait(self.web_driver, 10).until(
            expected_conditions.title_is('个人资料')
        )

class myQuestion(Base):
    PATH = '/userCenter/my/question'

    def is_me(self):
        return WebDriverWait(self.web_driver, 10).until(
            expected_conditions.title_is('我的提问')
        )

class myAnswer(Base):
    PATH = '/userCenter/my/answer'

    def is_me(self):
        return WebDriverWait(self.web_driver, 10).until(
            expected_conditions.title_is('我的解答')
        )
