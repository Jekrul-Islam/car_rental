from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User

from users.models import CarModel, appointment


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Password Again", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'})}


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True,
                                                           'class': 'form-control'}))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password',
                                          'class': 'form-control'}),
    )


class CreateCarForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = ('car_name', 'car_model', 'capacity')

    def __init__(self, *args, **kwargs):
        super(CreateCarForm, self).__init__(*args, **kwargs)


class ChooseCarForm(forms.ModelForm):
    class Meta:
        model = appointment
        fields = ('car',)

    def __init__(self, *args, **kwargs):
        super(ChooseCarForm, self).__init__(*args, **kwargs)
