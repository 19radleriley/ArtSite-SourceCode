"""
    Author: Riley Radle
    Description:
        models.py holds my custom database objects. Each of the 
        classes inherits from Django's Model class.  These objects
        are used to hold information about items in the store.
"""

from django.db import models

"""
    Models a category of items within the store 
"""
class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=200)

    # Allows the name of the category to display in admin page
    def __str__(self):
        return self.name

"""
    Models an item within the store
"""
class Item(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    
    # Path of the image within the project
    image = models.CharField(max_length=200)
    
    # description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_cart = models.BooleanField(default=False)

    # Category that this item fits into 
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)

    # Tags that allow for better querying when an item is searched for
    tags = models.TextField()

    description = models.JSONField(default=None, encoder=None, decoder=None)

    # Allows the name of the category to display in admin page
    def __str__(self):
        return self.name
