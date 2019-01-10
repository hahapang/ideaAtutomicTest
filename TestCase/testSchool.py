import unittest
from Webpage.SchoolePage import SchoolPage

class TestSchool(unittest.TestCase):
    def test_schoolpage(self):
        school_page = SchoolPage()
        try:
            school_page.open()
            assert "入驻高校" in school_page.web_driver.title

        finally:
            school_page.close()
