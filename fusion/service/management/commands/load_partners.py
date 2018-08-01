import json

from django.core.management.base import BaseCommand

from fusion.service.models import (Category, Comment, Contact, Engagement,
                                   Link, Partner, PartnerCategory)


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-i', dest='filename', required=True,
                            help='full path to the database dump to load')

    def handle(self, *args, **options):
        # Load all categories for their references by name
        categories = {}
        for c in Category.objects.all():
            categories[c.name] = c

        # Read the JSON file and parse into objects
        with open(options['filename'], 'r') as f:
            loaded = json.loads(f.read())

        # Load each partner read from the JSON file
        for x in loaded:
            self.load_partner(x, categories)

    @staticmethod
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
        for l_data in partner.get('links', []):
            link = Link(
                name=l_data['name'],
                url=l_data['url'],
                description=l_data['description'],
            )
            link.partner = p
            link.save()

        # Comments
        for c_data in partner.get('comments', []):
            comment = Comment(
                text=c_data
            )
            comment.partner = p
            comment.save()

        # Contacts
        for c_data in partner.get('contacts', []):
            contact = Contact(
                name=c_data['name'],
                email=c_data.get('email', None),
                role=c_data.get('role', None),
                notes=c_data.get('notes', None),
            )
            contact.partner = p
            contact.save()

        # Engagements
        for e_data in partner.get('engagements', []):
            engagement = Engagement(
                notes=e_data['notes'],
                location=e_data['location'],
                timestamp=e_data['timestamp'],
                attendees=e_data['attendees'],
            )
            engagement.partner = p
            engagement.save()
