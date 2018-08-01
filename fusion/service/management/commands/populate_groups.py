from django.core.management.base import BaseCommand

from django.contrib.auth.models import Group, Permission


EDITOR_CODENAMES = (
    'add_partner',
    'delete_partner',
    'change_partner',
    'add_comment',
    'delete_comment',
    'change_comment',
    'add_contact',
    'delete_contact',
    'change_contact',
    'add_engagement',
    'delete_engagement',
    'change_engagement',
    'add_partnercategory',
    'delete_partnercategory',
    'change_partnercategory',
    'add_link',
    'delete_link',
    'change_link',
)


class Command(BaseCommand):
    help = 'Adds the standard groups to the database'

    def handle(self, *args, **options):
        populate_groups()


def populate_groups():
    print('Populating groups...')
    g, created = Group.objects.get_or_create(
        name='Editors'
    )

    if created:
        for c in EDITOR_CODENAMES:
            permission = Permission.objects.get(codename=c)
            g.permissions.add(permission)
        g.save()
        print('  Added group: Editors')
    else:
        print('  Found group: Editors')

    g, created = Group.objects.get_or_create(
        name='Read Only'
    )
    if created:
        print('  Added group: Read Only')
    else:
        print('  Found group: Read Only')

    print('Completed!')
