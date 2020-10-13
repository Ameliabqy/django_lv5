import os

# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','my_first_proj.settings')

import django
# Import settings
django.setup()

from faker import Faker
from first_app.models import Name, User

def add_name(fn, ln):
    n = Name.objects.get_or_create(first_name=fn, last_name=ln)[0]
    n.save()
    return n

def populate_fake_users(num_users):
    faker = Faker()
    for i in list(range(num_users)):
        first_name = faker.first_name()
        last_name = faker.last_name()
        n = add_name(first_name, last_name)

        u = User.objects.get_or_create(top_name=n, email=faker.email())[0]
        u.save()

if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate_fake_users(50)
    print('Populating Complete')
