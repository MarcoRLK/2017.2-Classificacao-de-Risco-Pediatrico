# Arquivo: /apps/users/views.py
from django.shortcuts import render
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.core.urlresolvers import reverse_lazy, reverse

from .forms import RegistrationAdminForm
from .forms import RegistrationAttendantForm


def home(request):
    return render(request, 'users/home.html')


def login_view(request, *args, **kwargs):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('users:home'))

    kwargs['extra_context'] = {'next': reverse('users:home')}
    kwargs['template_name'] = 'users/login.html'
    return login(request, *args, **kwargs)


def logout_view(request, *args, **kwargs):
    kwargs['next_page'] = reverse('users:home')
    return logout(request, *args, **kwargs)


class RegistrationAdminView(CreateView):
    form_class = RegistrationAdminForm
    template_name = "users/registerStaff.html"
    success_url = reverse_lazy('users:login')


class RegistrationAttendantView(CreateView):
    form_class = RegistrationAttendantForm
    template_name = "users/registerStaff.html"
    success_url = reverse_lazy('users:login')
