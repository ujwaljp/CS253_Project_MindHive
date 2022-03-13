
from attr import fields
import django
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.urls import reverse
from .models import User
from django.views import generic
from .forms import Updateuserinfo
# Create your views here.

def profile(request,pk):
    usr = User.objects.get(pk=pk)
    return render(request, 'homepage.html', {'usr': usr})

def edit(request,user_id):
    usr = User.objects.get(id=user_id)
    return render(request, 'edit_profile.html', {'usr': usr})
class UserEditView(generic.UpdateView):
    model = User
    fields=["username","profile_image"]
    template_name = "edit_profile.html"
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('view_user', kwargs={'pk': self.object.id})
