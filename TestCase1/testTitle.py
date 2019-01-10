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
            asset_page = home_page.navigate_by_xpath(xpath='//*[@id="root"]/header/div/nav/a[2]', to_web_page=AssetPage)
            assert "作品" in asset_page.web_driver.title
        finally:
            home_page.close()

    def test_false(self):
        home_page = HomePage()
        try:
            home_page.open()
            assert "创想空间1" in home_page.web_driver.title
        finally:
            home_page.close()
