from django.http import JsonResponse
from .models import User, ActivityTrack
from django.views.generic import View
# Create your views here.


class UserActivityView(View):
    def get(self, *args, **kwargs):
        # get the data from User model
        users = User.objects.all()

        # create a data variable which will store the data
        data = {"ok": 'true', "members": []}

        # loop over each user and fetch user id, name, time zone
        # this will give all the members 
        for user in users:
            user_data = {}
            user_data["id"] = user.id # user id
            # concatenate the first and last name into real name
            real_name = user.first_name + " " + user.last_name
            user_data["real_name"] = real_name
            user_data['tz'] = user.tz # user's time zone
            # deine a list which will store the user's activity 
            user_data["activity_periods"] = []
            # filter all the activities for a given user by user id
            activities = ActivityTrack.objects.filter(user=user.id)
            user_activities = {}
            # loop over all the activities one by one 
            # this will give all the activity of a user
            for act in activities:
                user_activities["start_time"] = act.start_time # activity start time
                user_activities["end_time"] = act.end_time # activity end time
            user_data["activity_periods"].append(user_activities)
            data["members"].append(user_data)

        return JsonResponse(data)
