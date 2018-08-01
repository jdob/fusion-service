from django.contrib.auth.models import Group, User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Creates a series of test users'

    def handle(self, *args, **options):
        populate_test_users()


def populate_test_users():
    print('Populating test users...')

    # Admin
    u, created = User.objects.get_or_create(
        username='admin',
        password='admin',
        is_superuser=True
    )
    if created:
        print('  Added admin')
    else:
        print('  Found admin')

    # Read Only Users
    u, created = User.objects.get_or_create(
        username='readonly1',
        password='readonly1',
    )
    if created:
        readonly = Group.objects.get(name='Read Only')
        readonly.user_set.add(u)
        print('  Added readonly1')
    else:
        print('  Found readonly1')

    # Editors
    u, created = User.objects.get_or_create(
        username='editor1',
        password='editor1'
    )
    if created:
        editors = Group.objects.get(name='Editors')
        editors.user_set.add(u)
        print('  Added editor1')
    else:
        print('  Found editor1')

    print('Completed!')
