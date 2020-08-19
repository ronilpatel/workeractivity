from django.shortcuts import render
import requests
import json


def worker_activities(request):

    print('reached the views...hitting api started')

    url = 'http://127.0.0.1:8000/api/activity/all-worker/'

    print('hitting api ended.....')

    response = requests.get(url=url)

    response = json.loads(response.text)
    final_response = list()

    for member in response.get("members", ""):

        member_info = {}
        member_info["name"] = member.get("real_name","")
        member_info["time_zone"] = member.get("tz","")
        member_info["activity_periods"] = member.get("activity_periods", [])

        final_response.append(member_info)

    render(request=request, 
           template_name="worker/worker-activity.html",
           context={
               'worker-activity' : final_response
           })