from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView, UpdateView, CreateView,
                        DetailView, FormView, DeleteView)
import datetime
from .models import (User, Character, Weapon, PrimaryStatistics, DustPouch,
                    Skills)
from .forms import SignUpForm
from django.http import Http404

class UserCreate(CreateView):
    model = User
    form = SignUpForm()
    #fields = ['username', 'email', 'password', 'first_name', 'last_name']
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
