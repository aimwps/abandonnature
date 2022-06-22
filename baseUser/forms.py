from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from .models import ANUser


class ANUserCreationForm(UserCreationForm):
    first_name = forms.CharField(   max_length=30,
                                    required=True,
                                    widget=forms.TextInput( attrs = {   'class' : 'form-control',
                                                                        'placeholder': "*Your first name.."
                                                                    }),
    )
    last_name = forms.CharField(   max_length=30,
                                    required=True,
                                    widget=forms.TextInput( attrs = {   'class' : 'form-control',
                                                                        'placeholder': "*Your last name.."
                                                                    }),
    )
    password1 = forms.CharField(widget=forms.PasswordInput( attrs = {'class' : 'form-control',
                                                                    'placeholder': "*Password.."
                                                                }),
    )
    password2 = forms.CharField(widget=forms.PasswordInput( attrs = {   'class' : 'form-control',
                                                                        'placeholder': "*Confirm Password.."
                                                                    }),
    )
    email = forms.EmailField(max_length = 254,
                            required = True,
                            widget = forms.TextInput(attrs={'placeholder': "*Email..", "class":"form-control"}))

    token = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = ANUser
        fields = ("email","first_name","last_name", 'password1', 'password2',)

class ANUserChangeForm(UserChangeForm):
    class Meta:
        model = ANUser
        fields = ("email","first_name","last_name")

class ANUserLoginForm(AuthenticationForm):
    email = forms.EmailField(max_length=254, required=True,
                            widget=forms.TextInput(attrs={'placeholder': '*Email..', 'class' : 'form-control',}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "*Password..", 'class' : 'form-control',}))
    class Meta:
        model = ANUser
        fields= ('email', 'password')
