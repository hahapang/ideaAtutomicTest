import unittest
from Action.userLogin import Action
from Webpage.AssetDetail import AssetDetail
from Webpage import CreateAsset

class TestAssetDetail(unittest.TestCase):

    def test_asset_detail(self):
        home_page = Action.user_login_home(0)

        asset_detail = AssetDetail.jump_to_me(home_page, args='/' + id)
        assert "自动测试作品标题" in asset_detail.web_driver.title

        asset_detail.close()

