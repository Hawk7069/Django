import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

import random
from AppTwo.models import User
from faker import Faker

fake = Faker()

def populate(N=5):
    for i in range(N):
        fn = fake.first_name()
        ln = fake.last_name()
        em = fake.email()
        user = User.objects.get_or_create(first_name = fn, last_name = ln, email = em)

if __name__ == '__main__':
    print('Populating')
    populate(20)
    print('Populated')
