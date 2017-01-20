from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Populate School, Classroom and Student objects from enroll.fixtures'

    def _call_fixtures(self):
        '''
        Load fixtures in this order:
          - school.json
          - classroom.json
          - student.json
        '''
        from django.core.management import call_command
        call_command('loaddata', 'school')
        call_command('loaddata', 'classroom')
        call_command('loaddata', 'student')

    def handle(self, *args, **options):
        self._call_fixtures()
