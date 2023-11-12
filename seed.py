import random
from faker import Faker
fake = Faker()


def make_grades(count):
    return [
        {"name": fake.name(), "grade": random.randint(0, 10)} for _ in range(count)
    ]
