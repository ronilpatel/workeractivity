from django.core.management.base import BaseCommand
from faker import Faker
from worker.models import WorkerProfile


def delete_previous_profiles():
    profiles = WorkerProfile.objects.all()
    for profile in profiles:
        profile.delete()


class Command(BaseCommand):
    help = 'Populate the database....'
    def add_arguments(self, parser):
        parser.add_argument('--users',
                            default=50,
                            type=int,
                            help="No of fake workers to be created...")

    def handle(self, *args, **options):
        print('populating....')
        faker_obj = Faker()
        # delete_previous_profiles()
        for _ in range(options['users']):   
            firstname = faker_obj.first_name()
            lastname = faker_obj.last_name()
            timezn = faker_obj.timezone()
            wpf = WorkerProfile(firstname=firstname,
                                lastname=lastname,
                                timezn=timezn)
            wpf.save()
        print('done....')
