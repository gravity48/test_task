from unittest import IsolatedAsyncioTestCase

from database.database import Database
from tasks.course import SetCourseTask


class TestSetCourse(IsolatedAsyncioTestCase):

    def setUp(self):
        self.task = SetCourseTask(Database().session)

    async def test_010_get_data(self):
        result = await self.task()
        self.assertTrue(result)
