from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from django.http import HttpResponse

from worker.models import WorkerProfile, ActivityPeriod
# from django.contrib.auth import get_user_model

# User = get_user_model()


class WorkerActivity(APIView):

    def get(self, request):

        response = dict()

        response["ok"] = True
        response["members"] = list()
    
        workers = WorkerProfile.objects.all()

        if workers:
            date_time_format = '%b %d %Y %I:%M %p'

            for worker in workers:

                worker_activity = {}
                
                worker_activity["id"] = worker.workid
                worker_activity["real_name"] = worker.firstname + " " + worker.lastname
                worker_activity["tz"] = worker.timezn
                worker_activity["activity_periods"] = list()

                activities = worker.activityperiod_set.all()

                for activity in activities:
                
                    context = {}
                    context["start_time"] = activity.start.strftime(date_time_format)
                    context["end_time"] = activity.end.strftime(date_time_format)
                    worker_activity["activity_periods"].append(context)

                response["members"].append(worker_activity)

            print('respone data is : ', response)

            return Response(data=response,
                            status=status.HTTP_200_OK)

        else:
            
            return Response(data=response, status=status.HTTP_204_NO_CONTENT)