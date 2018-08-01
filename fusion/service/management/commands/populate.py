from django.core.management.base import BaseCommand

from .populate_categories import populate_categories
from .populate_groups import populate_groups


class Command(BaseCommand):
    help = 'Performs the initial database population'

    def handle(self, *args, **options):
        populate_categories()
        populate_groups()
        