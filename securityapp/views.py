from .models import Account
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.contrib.messages.views import SuccessMessageMixin


class IndexView(generic.ListView):
    template_name = 'securityapp/accounts_list.html'

    def get_queryset(self):
        return Account.objects.all()


class DetailView(generic.DetailView):
    model = Account
    template_name = 'securityapp/account_details.html'


class AccountCreate(SuccessMessageMixin, CreateView):
    model = Account
    fields = ['account_name', 'email', 'phone_number', 'user_first_name', 'user_last_name']
    success_message = "Account created successfully"


class AccountUpdate(SuccessMessageMixin, UpdateView):
    model = Account
    fields = ['account_name', 'email', 'phone_number', 'user_first_name', 'user_last_name']
    success_message = "Account updated successfully"


class AccountDelete(DeleteView):
    model = Account
    success_url = reverse_lazy('securityapp:index')


def logout_view(request):
    logout(request)
    return redirect('')




