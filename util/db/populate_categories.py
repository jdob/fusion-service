import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fusion.settings')
import django
django.setup()


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


class CategoryPopulator(object):

    @staticmethod
    def add_categories():
        print('Populating categories...')
        for name, description in CATEGORIES:
            print('  Adding category: %s' % name)
            c = Category(name=name, description=description)
            c.save()
        print('Completed!')


if __name__ == '__main__':
    populator = CategoryPopulator()
    populator.add_categories()
