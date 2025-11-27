from django.contrib import admin
from django.urls import include, path
from account_user.views import UserListView

urlpatterns = [
    path("", UserListView.as_view(), name="base")
]
