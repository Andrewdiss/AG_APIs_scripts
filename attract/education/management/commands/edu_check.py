from django.core.management.base import BaseCommand
from education.models import Document


class Command(BaseCommand):
    help = 'Returns list of people who have specified education'

    def add_arguments(self, parser):
        parser.add_argument('education',
                            help='Take one of listed educations as argument',
                            choices=['master', 'bachelor',
                                     'specialist', 'all'],
                            nargs=1,
                            )

    def handle(self, *args, **options):
        for education in options['education']:
            if education == 'all':
                doc_list = Document.objects.all()
            else:
                doc_list = Document.objects.filter(
                    person_education__icontains=education)
            for edu in doc_list:
                self.stdout.write('%s %s' % (edu.person_education.ljust(15),
                                             edu.person
                                             ))
