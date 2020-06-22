from django.urls import path
from activity import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<str:pk>', views.UserDetail.as_view()), 
    path('activities/', views.ActivityList.as_view()),
    path('activities/<str:pk>/<int:id>', views.ActivityDetail.as_view()),
    path('usersactivities/', views.UserActivityView.as_view()),
    
]
