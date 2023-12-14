from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Type your email here'}))

    password1 = forms.CharField(max_length=20, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['username'].widget.attrs['placeholder'] = 'User name'
