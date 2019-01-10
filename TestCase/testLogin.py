import unittest
from Webpage.Loginpage import LoginPage
from time import sleep
from Action.userLogin import Action

class TestLogin(unittest.TestCase):
     def test_login_load(self):
         def test_login_load(self):
             login_page = LoginPage()
             try:
                 login_page.open()
                 assert "用户登录" in login_page.web_driver.title
             finally:
                 login_page.close()

     def test_login_submit(self):

         try:
             login_page = Action.user_login_home(0)

         finally:

             login_page.close()

