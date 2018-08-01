import argparse
import json
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fusion.settings')
import django

django.setup()

from fusion.service.models import Partner


def dump_partners(filename):
    all_partners = []
    for p in Partner.objects.all():
        dumped = dump_partner(p)
        all_partners.append(dumped)

    as_s = json.dumps(all_partners, indent=4, sort_keys=True, default=str)
    with open(filename, 'w') as f:
        f.write(as_s)


def dump_partner(partner):
    p = {}

    p['name'] = partner.name
    p['summary'] = partner.summary
    p['logo'] = partner.logo
    p['created'] = partner.created
    p['updated'] = partner.updated
    p['categories'] = []
    p['links'] = []
    p['comments'] = []
    p['contacts'] = []
    p['engagements'] = []

    # Categories: many-to-many, this is gonna be handled differently
    for cat in partner.categories.all():
        p['categories'].append(cat.category.name)

    # Links
    for link in partner.links.all():
        l = {
            'name': link.name,
            'url': link.url,
            'description': link.description,
        }
        p['links'].append(l)

    # Comments
    for comment in partner.comments.all():
        p['comments'].append(comment.text)

    # Contacts
    for contact in partner.contacts.all():
        c = {
            'name': contact.name,
            'email': contact.email,
            'role': contact.role,
            'notes': contact.notes,
        }
        p['contacts'].append(c)

    # Engagements
    for engagement in partner.engagements.all():
        e = {
            'notes': engagement.notes,
            'location': engagement.location,
            'timestamp': engagement.timestamp,
            'attendees': engagement.attendees,
        }
        p['engagements'].append(e)

    return p


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', dest='filename', required=True)
    args = parser.parse_args()

    dump_partners(args.filename)

