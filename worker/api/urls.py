from django.urls import path
from worker.api import views

urlpatterns = [
    path('all-worker/', views.WorkerActivity.as_view(), name='worker-activity'),
]
