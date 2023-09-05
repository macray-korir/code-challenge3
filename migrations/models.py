from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///restaurants.db')

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    ratings = Column(Integer)

    customer = relationship('Customer')
    restaurant = relationship('Restaurant')
