from django.contrib import admin
from django.urls import path
from activity import views

urlpatterns = [
    path('get/', views.UserActivityView.as_view()),
]
