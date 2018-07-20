import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fusion.settings')
import django
django.setup()

from django.contrib.auth.models import (Group, User)


def delete_users():
    print('Deleting all users...')
    User.objects.all().delete()


def create_users():
    print('Creating users...')

    User.objects.create_user('admin', 'admin@dobtech.io', 'admin')
    print('  Created admin')

    User.objects.create_user('user1', 'admin@dobtech.io', 'user1')
    print('  Created user1')

    User.objects.create_user('user2', 'admin@dobtech.io', 'user2')
    print('  Created user2')


if __name__ == '__main__':
    create_users()
