
from attr import fields
import django
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.urls import reverse
from .models import User
from django.views import generic
from .forms import Updateuserinfo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from django.views.generic import CreateView
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/sign_up.html'


def profile(request,pk):
    usr = User.objects.get(pk=pk)
    if request.user.is_authenticated:
        return render(request, 'homepage.html', {'usr': usr, 'viewer': request.user})
    else:
        return render(request, 'homepage.html', {'usr': usr})


# def edit(request,user_id):
#     if request.user.is_authentcated:
#         usr = User.objects.get(id=user_id)
#
#         return render(request, 'edit_profile.html', {'usr': usr})
#     else:
#         return HttpResponse('You must be logged in')


class UserEditView(LoginRequiredMixin ,generic.UpdateView):
    model = User
    fields=["username","profile_image"]
    template_name = "users/edit_profile.html"
    login_url = '/users/login/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('users:view_user', kwargs={'pk': self.object.id})
