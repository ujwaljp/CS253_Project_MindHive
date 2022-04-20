from .models import User
from notifications.models import Notification
from .forms import addTagsForm, UserCreateForm

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.urls import reverse
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
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
# class SignUp(CreateView):
#     form_class = UserCreateForm
#     success_url = reverse_lazy('users:login')
#     template_name = 'users/sign_up.html'




def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your MindHive account.'
            message = render_to_string('users/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = UserCreateForm()
    return render(request, 'users/sign_up.html', {'form': form})# class-based view to add favourite tags

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

class addTagsView(LoginRequiredMixin, UpdateView):
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
        return reverse('home:view_home', )

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
class UserEditView(LoginRequiredMixin, UpdateView):
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
