from django.forms import ModelForm

from .models import Profile


class RegisterForm(ModelForm):

    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'email', 'password',
                  'phone']
