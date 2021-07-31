"""
    Author: Riley Radle
    Description:
        Views.py is responsible for routing to and from the html pages.
        This views.py handles the backend for user registration.
"""

from django.shortcuts import render, redirect # Refactor other project using redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm

"""
    Allows a user to register with the store
"""
def register(request):
    # Checking that the form was submitted
    if request.method == "POST":

        # Get the form information and check that it is valid
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Save the user into the database
            form.save() 
            username = form.cleaned_data.get("username")

            # Send a message to the frontend, and redirect user to the login page
            messages.success(request, f"Account successfully created! Please login {username}!")
            return redirect("login")

    else:
        form = UserRegistrationForm()
    return render(request, "Users/register.html", {"form" : form})

