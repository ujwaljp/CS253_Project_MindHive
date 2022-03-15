from .models import User
from .forms import addTagsForm, UserCreateForm

from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()

class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/sign_up.html'

class addTagsView(LoginRequiredMixin, generic.UpdateView):
    model = User
    form_class= addTagsForm
    # fields = ['favouriteTags']
    template_name = 'users/addtags.html'
    login_url = '/users/login'
    def get_object(self):
        return self.request.user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('users:view_user', kwargs={'pk': self.object.id})


def profile(request,pk):
    usr = User.objects.get(pk=pk)
    if request.user.is_authenticated:
        return render(request, 'homepage.html', {'usr': usr, 'viewer': request.user})
    else:
        return render(request, 'homepage.html', {'usr': usr})

def testview(request):
    return HttpResponse('<h1>Test page</h1>')

# def edit(request):
#     if request.method:
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
    # form = Updateuserinfo(request.POST)
    def get_object(self):
        return self.request.user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('users:view_user', kwargs={'pk': self.object.id})
