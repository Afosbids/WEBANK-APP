from django.urls import path
from .views import UserDetailView, UserListView, home

urlpatterns = [
    path('', home),
    path('user_list/', UserListView.as_view()),
    path('user_detail/', UserDetailView.as_view()),
]
