from Webpage.Base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class AssetDetail(Base):
    # path = TestAsset().test_create_asset()
    #
    PATH = '/asset'

    def __init__(self, assetID):
        if (assetID):
            self.PATH += assetID

    def is_me(self):
        return WebDriverWait(self.web_driver, 10).until(
            expected_conditions.title_is('自动测试作品标题')
        )
