#######################################################
# 
# Point.py
# Python implementation of the Class Point
# Generated by Enterprise Architect
# Created on:      26-Sep-2020 9:41:22 PM
# Original author: natha
# 
#######################################################
from sqlalchemy import Column
from FreeTAKServer.model.SQLAlchemy.Root import Base
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import ForeignKey


class Point(Base):
# default constructor  def __init__(self):  
    __tablename__ = "Point"
    PrimaryKey = Column(ForeignKey("Event.uid"), primary_key=True)
    ce = Column(String(100))
    hae = Column(String(100))
    lat = Column(Float)
    le = Column(String(100))
    lon = Column(Float)