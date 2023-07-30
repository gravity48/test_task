from datetime import date, timedelta
from typing import Tuple

from database.database import Database
from database.models import CourseModel
from fastapi import Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound


class ExchangeRates:
    def __init__(self, session_factory=Depends(Database().session)):
        self.session_factory = session_factory

    async def get_course(self, date_filter: date) -> Tuple[float, float]:
        async with self.session_factory as session:
            query = (
                select(CourseModel)
                .where(CourseModel.created_at >= date_filter)
                .where(CourseModel.created_at < date_filter + timedelta(days=1))
            )
            result = await session.scalars(query)
            try:
                instance = result.one()
                return instance.dollar, instance.euro
            except NoResultFound:
                raise HTTPException(status_code=400, detail="Course not found")
