from django.contrib import admin

from .models import WorkerProfile, ActivityPeriod


admin.site.register(WorkerProfile)
admin.site.register(ActivityPeriod)