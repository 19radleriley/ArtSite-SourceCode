"""
Author: Riley Radle
Descpription:
  Contains several useful functions that 
  are used in views.py.  File is mainly for 
  organizational purposes. 
"""

from ..models import Item, Category
from decimal import Decimal

# Used for quickly adding items to database
# from .categories import categories
# from .items import items

"""
    Tax and shipping rate.
    Currently shipping is a flat rate.
    This could be changed in the future
"""
tax_rate = 0.05
shipping = 5


"""
    Simple function to retrieve all of the items in the user's cart.
    This is determined by a boolean associated with each item.
"""
def get_cart_items():
    # Query the database of items and filter by in_cart being true
    cart = Item.objects.filter(in_cart=True)
    return cart

"""
    Function to retrieve all of the items associated with a specific category.
    @param name: The name of the category from which to get the items
"""
def get_category_items(name):
    # Query the database to get the category, then to get the items
    category = Category.objects.get(name=name)
    category_items = Item.objects.filter(category=category)
    return category_items

"""
    Function to query the database for items that the user searched for. 
    To have better searching, I added a 'tags' feature to each item and 
    listed common words associated with each item so it is easier for 
    the user to search rather than needing to browse.

    @param search_string: The string inputted by the user into the search bar
"""
def get_search_results(search_string):
    items = Item.objects.all()

    # Get all of the items where search_string is in the item tag
    # Down the road, I could use PostgreSQL or a third party software
    # for better querying.
    search_results = [
        item for item in items if search_string in item.tags
    ]

    return search_results


"""
    Simple function to add an item to cart.

    @param item: The item (database model) to add to the cart. 
"""
def add_to_cart(item):
    item.in_cart = True
    item.save()


"""
    Simple function to remove an item from the cart

    @param item: The item (database model) to remove from the cart. 
"""
def remove_from_cart(item):
    item.in_cart = False
    item.save()


"""
    Loop through the items in the cart and sum their prices to get a total price
"""
def sum_prices(cart):
    total = 0
    for item in cart:
        total += item.price
    
    return float(total)


"""
    The below functions are used to more quickly
    update the information in the database

    NOTE: MAKE SURE categories are FULLY added first
          because Item has a Category foreign key
"""


"""
    Function to add all of the categories into the database.
    The categories are stored in a list in categories.py
"""
def add_database_categories():
    for category in categories:
        category.save()


"""
    Function to add all of the items into the database.
    The items are stored in a list in items.py
"""
def add_database_items():
    for item in items:
        item.save()


"""
    TO QUICKLY FILL DATABASE:
    1. Delete all migrations and db.sqlite3 file
    2. In views.py, comment out
        from .models import Item, Category
        from .utils import utils
    3. Run the following commands 
        a. python manage.py makemigrations
        b. python manage.py migrate
        c. python manage.py createsuperuser
    4. In views.py uncomment 
        from .models import Item, Category
        from .utils import utils
        utils.add_database_categories()
    5. In utils.py uncomment
        from .categories import categories
    6. Run the server
    7. Repeat 4 - 6 for, but for the items
"""

