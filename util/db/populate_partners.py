import base64
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fusion.settings')
import django

django.setup()

from fusion.service.models import (Category, Link, Partner, PartnerCategory)

PARTNERS = (
    ('Dynatrace',
     'Software intelligence for the enterprise cloud. Deliver perfect software experiences with real-time intelligence into customer satisfaction and behavior, your applications, and the performance of your hybrid multi-cloud.',
     ['Monitoring & Logging'],
     [
         {
             'url': 'http://dynatrace.com',
             'name': 'Homepage',
         },
         {
             'url': 'https://blog.openshift.com/partner-spotlight-dynatrace/',
             'name': 'Partner Spotlight',
         },
     ],
     'dynatrace.png',
     ),
    ('Black Duck',
     "Black Duck's multi-factor open source detection capabilities, in conjunction with Black Duck KnowledgeBase™, the most comprehensive database of open source component, vulnerability, and license information, enable you to research open source projects, mitigate security and license compliance risks, and automatically enforce open source policies using your existing DevOps tools and processes.",
     ['Security'],
     [
         {
             'url': 'https://www.blackducksoftware.com/',
             'name': 'Homepage',
         },
     ],
     'blackduck.png',
     ),
    ('JFrog',
     "Universal Artifact Management for DevOps Acceleration",
     ['Development Tools'],
     [
         {
             'url': 'https://jfrog.com/',
             'name': 'Homepage',
         }
     ],
     'jfrog.png',
     ),
    ('Couchbase',
     "Couchbase Server is an open-source, distributed multi-model NoSQL document-oriented database software package that is optimized for interactive applications.",
     ['Database'],
     [
         {
             'url': 'https://www.couchbase.com/',
             'name': 'Homepage',
         },
     ],
     'couchbase.png'),
    ('NuoDB',
     "NuoDB’s elastic SQL database combines the elastic scale and continuous availability of the cloud with the transactional consistency and durability that databases of record demand.",
     ['Database'],
     [
         {
             'url': 'https://www.nuodb.com/',
             'name': 'Homepage',
         }
     ],
     'nuodb.jpg',
     ),
    ('Crunchy Data',
     "The trusted open source enterprise PostgreSQL leader providing certified PostgreSQL, support, and cloud-native, Kubernetes-based solutions.",
     ['Database'],
     [
         {
             'url': 'https://www.crunchydata.com/',
             'name': 'Homepage',
         },
     ],
     'crunchydata.png'),
    ('Twistlock',
     "Twistlock is the industry’s most complete, automated and scalable container cybersecurity platform. From precise, full-lifecycle vulnerability and compliance management to application-tailored runtime defense and cloud native firewalls, Twistlock secures your containers and modern applications against the next generation of threats across the entire application lifecycle.",
     ['Security'],
     [
         {
             'url': 'https://www.twistlock.com/',
             'name': 'Homepage',
         },
     ],
     'twistlock.jpg',
     ),
    ('CyberArk',
     "With the most complete solution in the industry, only CyberArk protects your enterprise from the ever-expanding attack surface by locking down privileged access: on-premises, in the cloud or in hybrid environments.",
     ['Security'],
     [
         {
             'url': 'https://www.cyberark.com/',
             'name': 'Homepage',
         },
     ],
     'cyberark.png',
     ),
    ('Aqua Security',
     "Aqua provides development-to-production security controls for cloud-native applications that run on-premises or on any cloud, on Windows, Linux or in on-demand container-as-a-service environments, using any orchestration platform.",
     ['Security'],
     [
         {
             'url': 'https://www.aquasec.com/',
             'name': 'Homepage',
         },
     ],
     'aquasec.jpg',
     ),
    ('6Fusion',
     "6fusion is an end-to-end digital supply chain Platform for IT that connects buyers and sellers using the power of rich analytics and algorithmic matching capabilities to help you better Measure, Analyze, and Transact in the era of IT Utility. We make smarter IT buyers and help IT sellers do more of what they do, faster.",
     ['Monitoring & Logging'],
     [
         {
             'url': 'http://6fusion.com/',
             'name': 'Homepage',
         },
     ],
     '6fusion.png'
     ),
    ('Splunk',
     "The fastest way to aggregate, analyze and get answers from your machine data.",
     ['Monitoring & Logging'],
     [
         {
             'url': 'https://www.splunk.com/',
             'name': 'Homepage',
         },
     ],
     'splunk.jpg'
     ),
    ('MongoDB',
     "MongoDB Enterprise Advanced features MongoDB Enterprise Server and a finely-tuned package of advanced software, support, certifications, and other services. More than one-third of the Fortune 100 rely on MongoDB Enterprise Advanced to help run their mission critical applications.",
     ['Database'],
     [
         {
             'url': 'https://www.mongodb.com/',
             'name': 'Homepage',
         },
     ],
     'mongodb.jpg'
     ),
    ('NetApp',
     "Trident is a fully supported open source project maintained by NetApp. It has been designed from the ground up to help you meet the sophisticated persistence demands of your containerized applications.",
     ['Data Services'],
     [
         {
             'url': 'http://www.netapp.com,https://github.com/NetApp/trident',
             'name': 'Homepage',
         },
     ],
     'netapp.png',
     ),
    ('PureStorage',
     "Pure Storage provides enterprise, all-flash data storage solutions that deliver data-centric architecture to accelerate your business for a competitive advantage.",
     ['Data Services'],
     [
         {
             'url': 'https://www.purestorage.com/',
             'name': 'Homepage',
         },
     ],
     'purestorage.png'
     ),
    ('Avi Networks',
     "The Avi Vantage Platform delivers a 100% software approach to application services with Software Load Balancers, Intelligent WAF & Elastic Service Mesh.",
     ['Networking'],
     [
         {
             'url': 'https://avinetworks.com/',
             'name': 'Homepage',
         },
     ],
     'avinetworks.jpg'
     ),
    ('NGINX',
     "NGINX accelerates content and application delivery, improves security, facilitates availability and scalability for the busiest web sites on the Internet.",
     ['Networking'],
     [
         {
             'url': 'https://www.nginx.com/',
             'name': 'Homepage',
         },
     ],
     'nginx.png'
     ),
)


class PartnerPopulator(object):

    def __init__(self) -> None:
        super().__init__()

        self.categories = {}  # mapping of name to Category

    def _load_categories(self):
        self.categories.clear()
        for c in Category.objects.all():
            self.categories[c.name] = c

    def add_partners(self):
        print('Populating partners...')

        self._load_categories()

        for x in PARTNERS:
            print('  Adding partner: %s' % x[0])
            self.add_partner(x[0], x[1], x[2], x[3], x[4])

        print('Completed!')

    def add_partner(self, name, summary, category_names, links, logo_filename):

        # General Data
        p = Partner(name=name,
                    summary=summary)

        # Logo
        if logo_filename:
            logo_filename = './logos/%s' % logo_filename
            with open(logo_filename, 'rb') as image_file:
                image_data = image_file.read()
                encoded = base64.b64encode(image_data)
                p.logo = encoded.decode('UTF-8')

        # Store now so we have it for the category mappings
        p.save()

        # Category
        for name in category_names:
            c = self.categories[name]
            pc = PartnerCategory(partner=p, category=c)
            pc.save()

        # Links
        for link in links:
            l = Link(url=link['url'],
                     name=link['name'])
            l.partner = p
            l.save()


if __name__ == '__main__':
    populator = PartnerPopulator()
    populator.add_partners()
