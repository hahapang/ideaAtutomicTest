import unittest
from Webpage.UserCenter import myAssetPage
from Webpage.UserCenter import myQuestion
from Webpage.UserCenter import myAssetCollection
from Webpage.UserCenter import myClass
from Webpage.UserCenter import myAnswer
from Webpage.UserCenter import myCourse
from Webpage.UserCenter import myCourseCollection
from Webpage.UserCenter import myLearning
from Webpage.UserCenter import myHomework
from Webpage.UserCenter import myMessagePage
from Webpage.UserCenter import myPassword
from Webpage.UserCenter import myProfile
from Action.userLogin import Action


class TestUsercenter(unittest.TestCase):

    def test_myAsset(self):

        login_page = Action.user_login_home(0)

        user_center = myAssetPage.jump_to_me(login_page)
        assert "我的作品" in user_center.web_driver.title

        user_center.close()

    def test_myMessage(self):

        login_page = Action.user_login_home(0)

        user_center = myMessagePage.jump_to_me(login_page)
        assert "互动信息" in user_center.web_driver.title

        user_center.close()

    def test_myCollection(self):
        login_page = Action.user_login_home(0)

        user_center = myAssetCollection.jump_to_me(login_page)
        assert "我收藏的作品列表" in user_center.web_driver.title

        user_center.close()

    def test_myCourseCollection(self):
        login_page = Action.user_login_home(0)

        user_center = myCourseCollection.jump_to_me(login_page)
        assert "我收藏的课程" in user_center.web_driver.title

        user_center.close()

    def test_myQuestion(self):
        login_page = Action.user_login_home(0)

        user_center = myQuestion.jump_to_me(login_page)
        assert "我的提问" in user_center.web_driver.title

        user_center.close()

    def test_myAnswer(self):
        login_page = Action.user_login_home(0)

        user_center = myAnswer.jump_to_me(login_page)
        assert "我的解答" in user_center.web_driver.title

        user_center.close()

    def test_myLearning(self):
        login_page = Action.user_login_home(0)

        user_center = myLearning.jump_to_me(login_page)
        assert "我学习的课程" in user_center.web_driver.title

        user_center.close()

    def test_myHomework(self):
        login_page = Action.user_login_home(0)

        user_center = myHomework.jump_to_me(login_page)
        assert "我的作业" in user_center.web_driver.title

        user_center.close()

    def test_myCourse(self):
        login_page = Action.user_login_home(0)

        user_center = myCourse.jump_to_me(login_page)
        assert "全部" in user_center.web_driver.title

    def test_myClass(self):
        login_page = Action.user_login_home(0)

        user_center = myClass.jump_to_me(login_page)
        assert "我的课时" in user_center.web_driver.title

        user_center.close()

    def test_myProfile(self):
        login_page = Action.user_login_home(0)

        user_center = myProfile.jump_to_me(login_page)
        assert "个人资料" in user_center.web_driver.title

        user_center.close()

    def test_myPassword(self):
        login_page = Action.user_login_home(0)

        user_center = myPassword.jump_to_me(login_page)
        assert "修改密码" in user_center.web_driver.title

        user_center.close()


