from django.http import JsonResponse
from .models import User, ActivityTrack
from django.views.generic import View
# Create your views here.


class UserActivityView(View):
    def get(self, *args, **kwargs):
        users = User.objects.all()

        data = {"ok": 'true', "members": []}

        for user in users:
            user_data = {}
            user_data["id"] = user.id
            real_name = user.first_name + " " + user.last_name
            user_data["real_name"] = real_name
            user_data['tz'] = user.tz
            user_data["activity_periods"] = []
            activities = ActivityTrack.objects.filter(user=user.id)
            user_activities = {}
            for act in activities:
                user_activities["start_time"] = act.start_time
                user_activities["end_time"] = act.end_time
            user_data["activity_periods"].append(user_activities)
            data["members"].append(user_data)

        return JsonResponse(data)
