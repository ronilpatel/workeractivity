from django.core.management.base import BaseCommand

from faker import Faker
import random
import pytz
from pytz import timezone

from worker.models import ActivityPeriod, WorkerProfile


class Command(BaseCommand):

    help = 'Populate the database....'

    def add_arguments(self, parser):

        parser.add_argument('--activity',
                            default=2,
                            type=int,
                            help="No of activity per worker...")
        parser.add_argument('--worker',
                            default=5,
                            type=int,
                            help="No of workers to be allocated randomly...")

    def handle(self, *args, **options):
        print('populating....')
        faker_obj = Faker()

        profiles = WorkerProfile.objects.all()
        worker_ids = [ profile.workid for profile in profiles ]

        for _ in range(options['worker']):   
            
            worker = WorkerProfile.objects.get(workid=worker_ids[random.randrange(0, len(worker_ids))])
            worker_time_zone = timezone(worker.timezn)

            for _ in range(options['activity']):

                start = faker_obj.past_datetime(start_date='-40d')
                start = worker_time_zone.localize(start)
                
                end = faker_obj.future_datetime(end_date='+40d')
                end = worker_time_zone.localize(end)

                acitivity = ActivityPeriod(worker=worker,
                                    start=start,
                                    end=end)
                acitivity.save()
        print('done!....')