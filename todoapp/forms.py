from django import forms
from .models import Todo
from django.contrib.auth.models import User

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ['title', 'text', 'important']

class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']

class SignupForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password', 'email']