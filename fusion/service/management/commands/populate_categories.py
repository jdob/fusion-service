from django.core.management.base import BaseCommand

from fusion.service.models import Category


CATEGORIES = (
    ('Security',
     'Identity, Compliance, API Management, Authentication, Scanning'),
    ('Monitoring & Logging',
     'Application Monitoring, Cluster Monitoring, Performance Management, Analytics'),
    ('Development Tools',
     'CI/CD, Build Tools, Source Control, Release Management, Test/QA Tools'),
    ('Management',
     'Orchestration, Automation, Cluster Control, Scheduling, Configuration Management, Policy Management'),
    ('Networking',
     'SDN, Load Balancing, Routing'),
    ('Database',
     'SQL, NoSQL, Hosted Database Services'),
    ('Data Services',
     'Data Stores, Volume Plugins, Backup, Big Data'),
    ('Middleware',
     'Messaging, BPM, Integration'),
)


class Command(BaseCommand):
    help = 'Adds the standard categories to the database'

    def handle(self, *args, **options):
        populate_categories()


def populate_categories():
    print('Populating categories...')
    for name, description in CATEGORIES:
        cat, created = Category.objects.get_or_create(name=name, description=description)
        if created:
            print('  Added category: %s' % name)
        else:
            print('  Found category: %s' % name)
    print('Completed!')
