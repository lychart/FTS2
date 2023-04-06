#######################################################
# 
# Event.py
# Python implementation of the Class Event
# Generated by Enterprise Architect
# Created on:      26-Sep-2020 12:18:51 PM
# Original author: natha
# 
#######################################################
from sqlalchemy import Column
from FreeTAKServer.model.SQLAlchemy.Root import Base, Root
from FreeTAKServer.model.SQLAlchemy.CoTTables.Detail import Detail
from FreeTAKServer.model.SQLAlchemy.CoTTables.Point import Point
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Event(Base, Root):
# default constructor  def __init__(self):  

    __tablename__ = "Event"
    uid = Column(String(100), primary_key=True, unique=True)
    how = Column(String(100))
    start = Column(String(100))
    type = Column(String(100))
    version = Column(String(100))
    point = relationship("Point", uselist=False, backref="Event", cascade="all, delete, merge, delete-orphan")
    detail = relationship("Detail", uselist=False, backref="Event", cascade="all, delete, merge, delete-orphan")