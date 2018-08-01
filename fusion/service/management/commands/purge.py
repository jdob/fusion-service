from django.contrib.auth.models import Group, User
from django.core.management.base import BaseCommand

from fusion.service.models import (Engagement, Category, Contact, Link, Partner, Comment, PartnerCategory)


class Command(BaseCommand):
    help = 'Clears the entire database; must be run with -f to execute'

    def add_arguments(self, parser):
        parser.add_argument('-f', dest='force', action='store_true',
                            help='confirms the delete should take place')
        parser.add_argument('-p', dest='partners', action='store_true',
                            help='if specified, all partner-related data will be deleted')
        parser.add_argument('-c', dest='categories', action='store_true',
                            help='if specified, all categories will be deleted')
        parser.add_argument('-g', dest='groups', action='store_true',
                            help='if specified, all groups will be deleted')
        parser.add_argument('-u', dest='users', action='store_true',
                            help='if specified, all users will be deleted')
        parser.add_argument('-a', dest='all', action='store_true',
                            help='if specified, all fusion-related data will be deleted')

    def handle(self, *args, **options):
        if not options['force']:
            print('This command must be run with -f to confirm deletion')
            return

        if options['partners'] or options['all']:
            print('Deleting all partner-related entries from the database...')
            self._purge(Partner)
            self._purge(Engagement)
            self._purge(Contact)
            self._purge(Comment)
            self._purge(Link)
            self._purge(PartnerCategory)

        if options['categories'] or options['all']:
            print('Deleting all categories from the database...')
            self._purge(Category)

        if options['groups'] or options['all']:
            print('Deleting all groups from the database...')
            self._purge(Group)

        if options['users'] or options['all']:
            print('Deleting all users from the database...')
            self._purge(User)

        print('Completed!')

    @staticmethod
    def _purge(cls):
        print('  Deleting %s...' % cls.__name__)
        cls.objects.all().delete()

