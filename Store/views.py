"""
    Author: Riley Radle
    Description:
    Views.py is responsible for routing to and from the html pages.
    It handles requests from the user, querying the database, and more.
    This is the main backend file which handles the information about the store.
"""

from django.shortcuts import render
from .models import Item, Category
from .utils import utils


"""
    NOTE: 
    @param 'request' is a string representation 
    of the request that is generated from the html pages.
    Each view get's their own request object.
"""

"""
    Render the home html page to the browser.
"""
def home(request):
    # DO NOT UNCOMMENT, used to quickly/automatically add items to database.
    # utils.add_database_categories()
    # utils.add_database_items()
    return render(request, "Store/pages/home.html")


"""
    Render the login html page to the browser.
""" 
def login(request):
    return render(request, "Store/pages/login.html")


"""
    Display all of the items that have the given category.
    @param name: The name of the category from which to get and display items. 
""" 
def view_category(request, name):
    # Get the items associated with the category for displaying
    data_to_display = {
        "category_items" : utils.get_category_items(name)
    }

    return render(request, "Store/pages/view_category.html", data_to_display)


"""
    Display the items that match the user's search. 
"""
def search_results(request): 

    # The user searched for an item.
    if request.method == "POST":
        data_to_display = {}

        # Strip the whitespace off of the user's search and make it lowercase
        # Then get the search results
        search_string = request.POST['searched_string'].strip().lower()
        search_results = utils.get_search_results(search_string)

        # Record the data for displaying
        data_to_display["search_string"] = search_string
        data_to_display["search_results"] = search_results

        return render(request, "Store/pages/search_results.html", data_to_display)

    # The user did not search for an item.
    return render(request, "Store/pages/search_results.html")


"""
    Display a single item and all of it's relevant information. 
    @param name: The name of the item to display.
"""
def view_item(request, name):

    # Query the database for the current item.
    current_item = Item.objects.get(pk=name)
    data_to_display = {
        "current_item" : current_item
    }

    # The user tried to add or remove an item from cart
    if request.method == "POST":

        # If the item was in the cart, the user is removing it
        if current_item.in_cart:
            utils.remove_from_cart(current_item)

        # Else they must have been adding the item
        else:
            utils.add_to_cart(current_item)
         
    return render(request, "Store/pages/view_item.html", data_to_display)


"""
    Display the items in the current user's cart.
    @param name: The name of an item to remove from cart (if the user wishes to do so) 
"""
def view_cart(request, name=None):

    # User wants to remove an item from the cart
    if request.method == "POST":
        item = Item.objects.get(pk=name)
        utils.remove_from_cart(item)

    # Get the cart items and determine the total
    cart = utils.get_cart_items()
    total = utils.sum_prices(cart)

    # Dictionary of data to display in the html
    data_to_display = {
        "cart" : cart,
        "total" : "%.2f"%total
    }

    return render(request, "Store/pages/view_cart.html", data_to_display)


"""
    Display the items in the user's cart for checking out. 
"""
def checkout(request):
    # Get the cart items and determine the total
    cart = utils.get_cart_items()
    total = utils.sum_prices(cart)

    # Determine the subtotal
    subtotal = total + (total * utils.tax_rate) + utils.shipping
    tax = total * utils.tax_rate 

    # Dictionary of data to display in the html
    data_to_display = {
        "cart" : cart,
        "total" : "%.2f"%total, 
        "subtotal" : "%.2f"%subtotal,
        "tax" : "%.2f"%tax,
        "shipping" : "%.2f"%utils.shipping 
    }    

    return render(request, "Store/pages/checkout.html", data_to_display)


"""
    Render the about page for the website. 
"""
def about(request):
    return render(request, "Store/pages/about.html")
