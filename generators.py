from faker import Faker

fake = Faker(locale="ru_RU")

def generate_login():
    return fake.user_name()

def generate_password(length=10):
    return fake.password(length=length, special_chars=False)

def generate_firstname():
    return fake.first_name()
