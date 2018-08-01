import argparse
import json
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fusion.settings')
import django

django.setup()

from fusion.service.models import (Category, Comment, Contact, Engagement,
                                   Link, Partner, PartnerCategory)


def load_partners(filename):

    # Load all categories for their references by name
    categories = {}
    for c in Category.objects.all():
        categories[c.name] = c

    # Read the JSON file and parse into objects
    with open(filename, 'r') as f:
        loaded = json.loads(f.read())

    # Load each partner read from the JSON file
    for x in loaded:
        load_partner(x, categories)


def load_partner(partner, categories):
    p = Partner(
        name=partner['name'],
        summary=partner['summary'],
        logo=partner['logo'],
        created=partner['created'],
        updated=partner['updated'],
    )
    p.save()

    # Create the category relationship
    for cat_name in partner['categories']:
        c = categories[cat_name]
        pc = PartnerCategory(partner=p, category=c)
        pc.save()

    # Links
    for l_data in partner['links']:
        link = Link(
            name=l_data['name'],
            url=l_data['url'],
            description=l_data['description'],
        )
        link.partner = p
        link.save()

    # Comments
    for c_data in partner['comments']:
        comment = Comment(
            text=c_data
        )
        comment.partner = p
        comment.save()

    # Contacts
    for c_data in partner['contacts']:
        contact = Contact(
            name=c_data['name'],
            email=c_data['email'],
            role=c_data['role'],
            notes=c_data['notes'],
        )
        contact.partner = p
        contact.save()

    # Engagements
    for e_data in partner['engagements']:
        engagement = Engagement(
            notes=e_data['notes'],
            location=e_data['location'],
            timestamp=e_data['timestamp'],
            attendees=e_data['attendees'],
        )
        engagement.partner = p
        engagement.save()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='filename', required=True)
    args = parser.parse_args()

    load_partners(args.filename)
