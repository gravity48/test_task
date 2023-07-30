import json

import aiohttp
from database.models import CourseModel, TaskExceptions


class BaseTask:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def __call__(self, *args, **kwargs):
        try:
            return await self.handler(*args, **kwargs)
        except Exception as e:
            async with self.session_factory() as session:
                exception = TaskExceptions(error=repr(e))
                session.add(exception)

    async def handler(self, *args, **kwargs):
        raise NotImplementedError


class SetCourseTask(BaseTask):
    async def handler(self, *args, **kwargs) -> bool:
        async with aiohttp.ClientSession() as session:
            async with session.get('https://www.cbr-xml-daily.ru/daily_json.js') as resp:
                response = await resp.text()
                result = json.loads(response)
        async with self.session_factory() as session:
            course = CourseModel(
                dollar=result['Valute']['USD']['Value'],
                euro=result['Valute']['EUR']['Value'],
            )
            session.add(course)
        return True
