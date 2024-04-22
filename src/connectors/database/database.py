from sqlalchemy import create_engine, Identity, Column, String, Integer, Float, Date
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime


Base = declarative_base()


class ExchangeTransaction(Base):
    __tablename__ = "transactions"

    id = Column("id", Integer, Identity(start=1, cycle=True), primary_key=True)
    currency = Column("currency", String)
    rate = Column("rate", Float)
    price_in_pln = Column("price_in_pln", Float)
    date = Column("date", Date)

    def __init__(self, currency, rate, price_in_pln, date=datetime.today()):
        self.currency = currency
        self.rate = rate
        self.price_in_pln = price_in_pln
        self.date = date

    def __repr__(self):
        return f'({self.id}, {self.currency}, {self.rate}, {self.price_in_pln}, {self.date})'    
