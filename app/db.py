from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://sql9244283:bHnU6PW6AW@sql9.freemysqlhosting.net:3306/sql9244283'

#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://sql3245126:Nc7QzXqKx1@sql3.freemysqlhosting.net:3306/sql3245126'
#Just another one (Michael)

Base = declarative_base()

engine = create_engine(SQLALCHEMY_DATABASE_URI)

Session = sessionmaker(bind=engine)
session = Session()
