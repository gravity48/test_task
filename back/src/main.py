from contextlib import asynccontextmanager
from datetime import date

import uvicorn
from apscheduler.triggers.cron import CronTrigger
from database.database import Database
from fastapi import Depends, FastAPI
from pydantic import BaseModel
from services.exchange_rates import ExchangeRates
from settings import scheduler
from starlette.middleware.cors import CORSMiddleware
from tasks.course import SetCourseTask


@asynccontextmanager
async def lifespan(app: FastAPI):
    scheduler.add_job(
        SetCourseTask(Database().session).__call__,
        CronTrigger.from_crontab('0 0 * * *'),
        id='update_course',
    )
    scheduler.start()
    yield
    scheduler.shutdown()


app = FastAPI(lifespan=lifespan)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class CourseModel(BaseModel):
    dollar: float
    euro: float


@app.get('/')
async def course(date_filter: date, exchange_rates=Depends(ExchangeRates)) -> CourseModel:
    dollar, euro = await exchange_rates.get_course(date_filter)
    return CourseModel(dollar=dollar, euro=euro)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
