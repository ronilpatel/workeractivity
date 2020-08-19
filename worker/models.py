import factory
import factory.django
import uuid

from faker import Faker

from django.db import models


class WorkerProfile(models.Model):

    workid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, default='Warner', blank=True, null=True)
    timezn = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.firstname + "  " + self.lastname


class ActivityPeriod(models.Model):
    
    start = models.DateTimeField()
    end = models.DateTimeField()

    worker = models.ForeignKey(WorkerProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.worker.firstname + "\t" + str(self.start.strftime("%b %d %Y %I:%M%p"))


# "Jun 28 2018 at 7:40AM" -> "%b %d %Y at %I:%M%p"
# "September 18, 2017, 22:19:55" -> "%B %d, %Y, %H:%M:%S"
# "Sun,05/12/99,12:30PM" -> "%a,%d/%m/%y,%I:%M%p"
# "Mon, 21 March, 2015" -> "%a, %d %B, %Y"
# "2018-03-12T10:12:45Z" -> "%Y-%m-%dT%H:%M:%SZ"

# d.strftime("%B %d, %Y")
# > 'January 10, 1984'

# d.strftime("%Y/%m/%d")
# > '1984/01/10'

# d.strftime("%d %b %y")
# > '10 Jan 84'

# d.strftime("%Y-%m-%d %H:%M:%S")
# > '1984-01-10 23:30:00'

# new_date = asia.localize(datetime(2002, 10,27,6,0,0))
# >>> fmt = '%b %d %Y %I:%M %p'
# >>>
# >>>
# >>> new_date.strftime(fmt)
# 'Oct 27 2002 06:00 AM'
# >>> type(new_date.strftime(fmt))
# <class 'str'>