import unittest
from Webpage.HomePage import HomePage
from Webpage.AssetPage import AssetPage



class TestTitle(unittest.TestCase):
    def test_success(self):
        home_page = HomePage()
        try:
            home_page.open()
            assert "美科学院" in home_page.web_driver.title

            asset_page = AssetPage.jump_to_me(context=home_page)
            assert "作品展" in asset_page.web_driver.title
        finally:
            home_page.close()

    def test_click_link(self):
        home_page = HomePage()
        try:
            home_page.open()
            #asset_page = home_page.navigate_by_xpath(AssetPage,xpath='//*[@id="root"]/div[1]/header/div/nav/a[2]')
            asset_page = home_page.navigate_by_link(AssetPage,"作品展")
            assert "作品展" in asset_page.web_driver.title
        finally:
            home_page.close()

    def test_false(self):
        home_page = HomePage()
        try:
            home_page.open()
            assert "美科学院" in home_page.web_driver.title
        finally:
            home_page.close()