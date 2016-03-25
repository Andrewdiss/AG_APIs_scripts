from django.core.management.base import BaseCommand
from education.models import Document


class Command(BaseCommand):
    help = "Returns List of people who have specified education"

    def add_arguments(self, parser):
        parser.add_argument('education', type=str, help="master/bachelor/specialist")

    def handle(self, education, **options):
        doc_list = Document.objects.filter(person_education__icontains=education)
        for edu in doc_list:
            self.stdout.write("%s %s" % (edu.person_education.ljust(15), edu.person_id))
