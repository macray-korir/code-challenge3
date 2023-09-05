from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import Base, engine, Customer, Restaurant, Review
import random

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
fake = Faker()

# Create customers
customers = []
for _ in range(20):
    customer = Customer(
        first_name=fake.first_name(),
        last_name=fake.last_name()
    )
    session.add(customer)
    customers.append(customer)

# Create restaurants
restaurant_names = ["Restaurant A", "Restaurant B", "Restaurant C"]
restaurants = []
for name in restaurant_names:
    restaurant = Restaurant(
        name=name,
        price=random.randint(10, 100)
    )
    session.add(restaurant)
    restaurants.append(restaurant)

# Create reviews
for customer in customers:
    for _ in range(2):
        review = Review(
            customer_id=customer.id,
            restaurant_id=random.choice(restaurants).id,
            ratings=random.randint(1, 5)
        )
        session.add(review)

session.commit()
