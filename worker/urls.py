from django.urls import path
from .views import worker_activities

urlpatterns = [
    path('all-worker/', worker_activities, name='worker-activity'),
]
