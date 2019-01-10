import unittest
from Webpage.ToolsPage import KitPage
from Webpage.ToolsPage import ModulePage
from Webpage.ToolsPage import SoftListPage

class TestTools(unittest.TestCase):
    def test_kitPage(self):
        kit_page = KitPage()
        try:
            kit_page.open()
            assert "套件" in kit_page.web_driver.title

        finally:
            kit_page.close()

    def test_modulePage(self):
        module_page = ModulePage()
        try:
            module_page.open()
            assert "模块" in module_page.web_driver.title

        finally:
            module_page.close()

    def test_softListPage(self):
        softlist_page = SoftListPage()
        try:
            softlist_page.open()
            assert "软件下载" in softlist_page.web_driver.title

        finally:
            softlist_page.close()

