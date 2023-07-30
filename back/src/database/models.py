from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Index, Integer, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class CourseModel(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.now, index=True)
    dollar = Column(Float)
    euro = Column(Float)

    __table_args__ = (Index('gps_report_timestamp_device_id_idx', created_at.desc()),)


class TaskExceptions(Base):
    __tablename__ = 'exceptions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.now)
    error = Column(Text)
