import json

from django.core.management.base import BaseCommand

from fusion.service.models import Partner


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-o', dest='filename', required=True,
                            help='full path to the file to save the database dump')

    def handle(self, *args, **options):
        print('Dumping the partners to JSON...')

        # Convert each partner into a dict representation
        all_partners = []
        for p in Partner.objects.all():
            dumped = self.dump_partner(p)
            all_partners.append(dumped)

        # Convert the data into a JSON document
        as_s = json.dumps(all_partners, indent=4, sort_keys=True, default=str)

        # Save the dump
        with open(options['filename'], 'w') as f:
            f.write(as_s)

        print('Completed!')

    @staticmethod
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
