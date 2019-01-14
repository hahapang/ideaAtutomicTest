from Webpage.Loginpage import LoginPage
from Webpage.HomePage import HomePage

class Action():
    @staticmethod
    def user_login_home(index):
        login_page = LoginPage()
        login_page.open()

        login_page.input_login_info(index)

        #return login_page.navigate_by_xpath(xpath='//*[@id="root"]/div[2]/div/div/div/div/div/form/label/button', to_web_page=HomePage)
        return login_page.navigate_by_className(HomePage,"mic-btn")

