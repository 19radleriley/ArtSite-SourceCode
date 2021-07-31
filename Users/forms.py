"""
    Author: Riley Radle
    Description:
        forms.py holds a custom form which is used for registering
        a new user.  This form inherits from UserCreationForm and 
        simply adds an email field. 
"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

"""
    Custom form class for registering a user with the store
"""
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    # Meta data for the form
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]