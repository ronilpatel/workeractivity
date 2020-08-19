from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/activity/', include('worker.api.urls')),
    path('activity/', include('worker.urls'))

]
