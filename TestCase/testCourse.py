import unittest
from Action.userLogin import Action
from Webpage.CreateCourse import CreateCourse
from Webpage.UserCenter import myCourse
from Webpage.CoursePage import CoursePage
from time import sleep
import re

class TestCourse(unittest.TestCase):
    def test_course(self):
        course_page = CoursePage()
        try:
            course_page.open()
            assert "课程" in course_page.web_driver.title
        finally:
            course_page.close()

    def test_create_course(self):
        home_page = Action.user_login_home(0)

        create_course = CreateCourse.jump_to_me(home_page)
        assert "创建课程" in create_course.web_driver.title

        create_course.input_course_info(0)

        create_course.add_class_info()

        sleep(1)

        course_web = create_course.navigate_by_xpath(xpath='//*[@id="root"]/div[1]/div/div[2]/span/div[2]/input', to_web_page=myCourse)

        # Obtain Course id_href
        try:

            course_id_href = course_web.find_by_xpath('//div[@class="card course"][1]/a').get_attribute('href')

            print('====>',course_id_href)

        except Exception as error:

            print('Xpath语句有误，请检查！\nError:{}'.format(error))

        else:

            # Use Re Obtain course id
            course_id = re.search(r'/course/(.*)', course_id_href)
            if course_id:

                courseID = course_id.group(1)

                print('----->', courseID)

                return courseID

            else:

                print('未获取课程ID')

        create_course.close()
