import unittest
from Webpage.CreateAsset import CreateAsset
from Webpage.UserCenter import myAssetPage
from Action.userLogin import Action
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class TestAsset(unittest.TestCase):

    def test_create_asset(self):
        home_page = Action.user_login_home(0)

        create_asset = CreateAsset.jump_to_me(home_page)
        assert "创建作品" in create_asset.web_driver.title

        create_asset.input_asset_info(0)

        asset_web = create_asset.navigate_by_xpath(xpath = '//*[@id="root"]/div[2]/div/div[2]/label[2]/input', to_web_page=myAssetPage)

        WebDriverWait(self.web_driver, 10).until(EC.title_contains('作品'))

        # Obtain Asset id_href
        # try:
        #
        #     asset_id_href = asset_web.find_by_xpath('//div[@class="card asset"][1]/a').get_attribute('href')
        # except Exception as error:
        #
        #     print('Xpath语句有误，请检查！\nError:{}'.format(error))
        #
        # else:
        #
        #     # Use Re Obtain asset id
        #     asset_id = re.search(r'/asset/(.*)', asset_id_href)
        #     if asset_id:
        #
        #         assetID = asset_id.group(1)
        #         return assetID
        #
        #     else:
        #         print('未获取作品ID')
        #
        # create_asset.close()

