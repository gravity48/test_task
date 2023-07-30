import json
from unittest.mock import AsyncMock

from fastapi.testclient import TestClient
from unittest import IsolatedAsyncioTestCase, mock

from main import app


class TestSetCourse(IsolatedAsyncioTestCase):
    url = '/'

    async def asyncSetUp(self) -> None:
        self.client = TestClient(app)

    @mock.patch('services.exchange_rates.ExchangeRates.get_course', new_callable=AsyncMock)
    async def test_010_valid_endpoint(self, get_course):
        get_course.return_value = (1, 2)
        response = self.client.get(self.url, params={
            'date_filter': '2020-09-09',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual({'dollar': 1.0, 'euro': 2.0},json.loads(response.content))

    async def test_020_not_exist_course(self):
        response = self.client.get(self.url, params={
            'date_filter': '2100-09-09',
        })
        self.assertEqual(response.status_code, 400)
