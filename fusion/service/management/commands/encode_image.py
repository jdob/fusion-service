import base64

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-i', dest='filename', required=True,
                            help='full path to the image to encode')
        parser.add_argument('-o', dest='output',
                            help='full path to save the encoded image to')

    def handle(self, *args, **options):
        print('Encoding: %s' % options['filename'])
        encoded = encode(options['filename'])

        if options['output']:
            print('Saving encoded image to: %s' % options['output'])
            with open(options['output'], 'w') as f:
                f.write(encoded)
        else:
            print()
            print(encoded)


def encode(filename):
    with open(filename, 'rb') as image_file:
        image_data = image_file.read()
        encoded = base64.b64encode(image_data)

    encoded_s = encoded.decode('UTF-8')
    return encoded_s

