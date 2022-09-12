from django.urls import reverse
from django.views import generic
from django.contrib.auth import get_user_model
from .forms import UserForm

User = get_user_model()


class UserCreateView(generic.CreateView):
    form_class = UserForm
    template_name = 'registration/register.html'
    model = User


    def get_success_url(self):

        return reverse('login')


