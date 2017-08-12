from .models import Account
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .forms import UserForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


#@login_required(login_url="login/")
def home(request):
    return render(request, "securityapp/accounts_list.html")


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'securityapp/accounts_list.html'

    def get_queryset(self):
        queryset_list =  Account.objects.all()

        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(account_name__icontains=query) |
                Q(email__icontains=query) |
                Q(user_first_name=query) |
                Q(user_first_name=query)
            ).distinct()
        return queryset_list


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
    return redirect('login')


class UserFormView(SuccessMessageMixin, View):
    form_class = UserForm
    template_name = 'registration/registration_form.html'
    success_message = "Created successfully"

    # Get new form to create a user(sign up)
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # Sign in
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # return user objects if credentials are true
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return render(request, 'securityapp/newuser_welcome.html')

        return render(request, self.template_name, {'form': form})




