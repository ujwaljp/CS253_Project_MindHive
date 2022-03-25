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
from django.contrib.auth.decorators import login_required
from notifications.models import Notification
# Create your views here.

User = get_user_model()

# view function for showing the notifications
@login_required(login_url='/users/login')
def notifs_display(request):
    notifs = Notification.objects.filter(receiver__pk = request.user.id)
    # print(Notification.objects.all()[0].receiver)
    print(len(notifs))
    Notification.objects.filter(receiver__pk=request.user.id).delete()
    print("deleted notifications")
    return render(request, 'users/notifs.html', {'notifications': notifs})

# class-based view for signing up
class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/sign_up.html'

# class-based view to add favourite tags
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

# view function to view profile
def profile(request,pk):
    usr = User.objects.get(pk=pk)
    if request.user.is_authenticated:
        return render(request, 'homepage.html', {'usr': usr, 'viewer': request.user})
    else:
        return render(request, 'homepage.html', {'usr': usr})

def testview(request):
    return HttpResponse('<h1>Test page</h1>')

def users_list_view(request):
    users = []
    cnt = 0
    user_row = []
    for user in User.objects.all():
        user_row.append(user)
        cnt += 1
        if cnt % 3 == 0 or cnt == User.objects.count():
            users.append(user_row)
            user_row = []
    return render(request, 'users/users_list.html', {'users': users})

# view function to edit the user info
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
