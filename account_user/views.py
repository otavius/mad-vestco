from django.shortcuts import render, redirect 
from account_user.models import UserProfile
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
class UserListView(LoginRequiredMixin, ListView):
    template_name = "account_user/base.hmtl"
    model = UserProfile
    context_object_name = "user"