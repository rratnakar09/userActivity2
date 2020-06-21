from django.db import models

# Create your models here.


class User(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    tz = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.id


class ActivityTrack(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.CharField(max_length=50)
    end_time = models.CharField(max_length=50)

    def __str__(self):
        return self.user.id
