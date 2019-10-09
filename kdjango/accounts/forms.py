from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# UserCreationForm does not provide an email field.
# SignUpForm will extend it, and add an `email` field.
class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')