import os
from dotenv import load_dotenv

from sqlalchemy.orm import Session

from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, SmallInteger

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from datetime import datetime
load_dotenv()

dbuser = os.getenv('DBUSER')
dbpassword = os.getenv('DBPASSWORD')
dbhost = os.getenv('DBHOST')
dbname = os.getenv('DBNAME')



engine = create_engine(f"postgresql+psycopg2://{dbuser}:{dbpassword}@{dbhost}/{dbname}")

engine.connect()

session = Session(bind=engine)

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(200), nullable=False)
    
class Task(Base):
        __tablename__ = 'tratata'
        id = Column(Integer(), primary_key=True)
        name = Column(String(5), unique=True)


my_cust = Customer(
        first_name = "Shtopor",
        last_name = "BRO",
        username = "EL BABAYKO",
        email = "a-kol.80@mail.ru"       
)
session.add(my_cust)
# my_user = Task(
#         name = "ivan"
# )
# session.add(my_user)
session.commit()
# Base.metadata.create_all(engine)
