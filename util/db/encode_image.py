import base64
import sys


def encode(filename):
    with open(filename, 'rb') as image_file:
        image_data = image_file.read()
        encoded = base64.b64encode(image_data)

    encoded_s = encoded.decode('UTF-8')
    return encoded_s


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: %s $FILENAME' % sys.argv[0])
        sys.exit(1)

    filename = sys.argv[1]
    print('Encoding: %s' % filename)

    encoded = encode(filename)
    print(encoded)
