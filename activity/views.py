from activity.models import User, ActivityTrack
from activity.serializers import UserSerializer, ActivityTrackSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

from django.http import JsonResponse
from django.views.generic import View

from rest_framework import generics, mixins

# created a UserActivityView to get the user and their activities details
# this is same as the json format given in assignment.
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


# Create a mixins based userlist view which will be used to 
# get/post all user details 
class UserList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request): 
        return self.create(request)

# Create a mixins based ActivityList view which will be used to 
# get/post all the activity details 
class ActivityList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = ActivityTrack.objects.all()
    serializer_class = ActivityTrackSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request): 
        return self.create(request)
    

# Create a class based ActivityDetail view which will be used to 
# get/post/delete an user details based on user_id 
class UserDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, pk):
        print(pk)
        return self.retrieve(request, pk)
    
    def put(self, request, pk): 
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)    


# Create a class based ActivityDetail view which will be used to 
# get/post/delete an activity details based on user_id and activity_id 
class ActivityDetail(APIView):
    def get_object(self, pk, id):
        try:
            return ActivityTrack.objects.get(user_id=pk, id=id)
        except User.DoesNotExist:
            raise Http404    

    def get(self, request, pk, id):
        activity = self.get_object(pk, id)
        serializer = ActivityTrackSerializer(activity)
        return Response(serializer.data)
    
    def post(self, request, pk, id):
        activity = self.get_object(pk, id)
        serializer = ActivityTrackSerializer(activity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)    
  
    def delete(self, request, pk, id):
        activity = self.get_object(pk, id)
        activity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)     
