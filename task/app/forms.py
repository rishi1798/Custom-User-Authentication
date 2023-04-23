from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm,PasswordResetForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    contact = forms.CharField(max_length=15, required=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'contact', 'password1', 'password2')


class CustomAuthenticationForm(AuthenticationForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'password')


class CustomUserChangeForm(UserChangeForm):
    password=None

    class Meta:
        model = CustomUser
        fields =['email','contact','bio','address','full_name']

class CustomPasswordResetForm(PasswordResetForm):

    def get_users(self, email):
        return CustomUser.objects.filter(email__iexact=email,is_active=True)
    
