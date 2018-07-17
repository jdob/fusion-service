import base64
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fusion.settings")
import django
django.setup()

'''

DEPRECATED: Use populate.py instead.

'''


from fusion.service.models import (Engagement, Category, Contact, Partner, Comment, Category, PartnerCategory)


def _create_partner(key, links=None):
    pp = Partner()
    pp.name = 'Partner %s' % key
    pp.summary = 'Summary data about partner %s' % key
    pp.links = links

    # For now, use the Red Hat logo for all of them
    with open('red_hat_logo.jpg', 'rb') as image_file:
        image_data = image_file.read()
        encoded = base64.b64encode(image_data)
        pp.logo = encoded.decode('UTF-8')

    return pp


def _create_contact(key):
    cc = Contact()
    cc.name = 'Contact %s' % key
    cc.email = 'contact%s@company.com' % key
    cc.role = 'Role %s' % key
    return cc


def _create_engagement(key):
    ee = Engagement()
    ee.notes = 'Engagement notes %s' % key
    ee.location = 'Location %s' % key
    ee.attendees = 'foo,bar,baz'
    return ee


def _create_comment(key):
    comment = Comment()
    comment.text = 'Comment %s' % key
    return comment


def _create_category(key):
    category = Category()
    category.name = 'Category %s' % key
    category.description = 'Category %s' % key
    return category


def populate():
    print('Populating sample data...')

    print('  Creating categories...')
    categories = []
    for i in range(0, 3):
        c = _create_category(i)
        c.save()
        categories.append(c)
        print('    Created: %s' % c.name)

    print(' Creating partners...')

    # Partner 1
    p = _create_partner('1', links=['p1.com', 'p2.com'])
    p.save()
    partner_category = PartnerCategory()
    partner_category.partner = p
    partner_category.category = categories[0]
    partner_category.save()
    for i in range(1, 4):
        c = _create_contact(i)
        c.partner = p
        c.save()
    for i in range(1, 3):
        e = _create_engagement(i)
        e.partner= p
        e.save()
    for i in range(1,4):
        newComment = _create_comment(i)
        newComment.partner = p
        newComment.save()
    print('    Created: %s' % p.name)

    # Partner 2
    p = _create_partner('2')
    p.save()
    partner_category = PartnerCategory()
    partner_category.partner = p
    partner_category.category = categories[1]
    partner_category.save()
    e = _create_engagement('2')
    e.partner = p
    e.save()
    print('    Created: %s' % p.name)

    # Partner 3
    p = _create_partner('3')
    p.save()
    c = _create_contact('3')
    c.partner = p
    c.save()
    print('    Created: %s' % p.name)

    # Partner 4
    p = _create_partner('4')
    p.save()
    partner_category = PartnerCategory()
    partner_category.partner = p
    partner_category.category = categories[0]
    partner_category.save()
    partner_category = PartnerCategory()
    partner_category.partner = p
    partner_category.category = categories[1]
    partner_category.save()

    print('Completed!')


if __name__ == '__main__':
    populate()
