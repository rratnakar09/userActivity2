from django.db import models

# Create your models here.
# User model will have fields like user id, user first name, user last name and user timezone
class User(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    tz = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.id

# ActivityTrack model will have user start time and end time. 
class ActivityTrack(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.CharField(max_length=50)
    end_time = models.CharField(max_length=50)

    def __str__(self):
        return self.user.id
