from django.contrib.auth.models import Group, User
from django.core.management.base import BaseCommand

from fusion.service.models import (Engagement, Category, Contact, Link, Partner, Comment, PartnerCategory)


class Command(BaseCommand):
    help = 'Clears the entire database; must be run with -f to execute'

    def add_arguments(self, parser):
        parser.add_argument('-f', dest='force', action='store_true')
        parser.add_argument('-a', dest='all', action='store_true',
                            help='If specified, categories and groups will be deleted as well')

    def handle(self, *args, **options):
        if not options['force']:
            print('This command must be run with -f to confirm deletion')
        else:
            print('Deleting all partner-related entries from the database...')

            self.delete_all()

            if options['all']:
                print('Deleting categories and groups from the database...')
                self._purge(Category)
                self._purge(Group)
                self._purge(User)

            print('Completed!')

    @staticmethod
    def _purge(cls):
        print('  Deleting %s...' % cls.__name__)
        cls.objects.all().delete()

    def delete_all(self):

        self._purge(Partner)
        self._purge(Engagement)
        self._purge(Contact)
        self._purge(Comment)
        self._purge(Link)
        self._purge(PartnerCategory)

