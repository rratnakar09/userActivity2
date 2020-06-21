from django.contrib import admin
from django.urls import path
from activity import views

urlpatterns = [
    path('', views.UserActivityView.as_view()),
]
