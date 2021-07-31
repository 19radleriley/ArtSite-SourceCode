"""
    Author: Riley Radle
    Description: 
        admin.py allows me to 'register' database models with 
        the Django provided admin page.  By doing so, a superuser
        is able to manipulate database models from the admin page
        rather than needing to do so through through code. 
        This makes database management super quick and easy.
"""

from django.contrib import admin
from .models import Item, Category

# Register Item and Category
admin.site.register(Item)
admin.site.register(Category)
