from django.urls import path
from .views import UserDetailView, UserListView, home

urlpatterns = [
    path('', home),
    path('api/v1/users/all', UserListView.as_view()),
    path('api/v1/users/<int:pk>/', UserDetailView.as_view()),
]
