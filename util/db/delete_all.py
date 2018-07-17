import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fusion.settings")
import django
django.setup()


from fusion.service.models import (Engagement, Category, Contact, Partner, Comment, PartnerCategory)


def _purge(cls):
    print('  Deleting %s...' % cls.__name__)
    cls.objects.all().delete()

def delete_all():
    print('Deleting all entries from the database...')

    _purge(Partner)
    _purge(Category)
    _purge(Engagement)
    _purge(Contact)
    _purge(Comment)
    _purge(PartnerCategory)

    print('Completed!')


if __name__ == '__main__':
    delete_all()
