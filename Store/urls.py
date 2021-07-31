"""
    Author: Riley Radle
    Description: 
        Contains the url routes which link the html pages with views.py
        This is how django knows which pages to render.  
        The first parameter in 'path' is the url which will 
        appear in the address bar of the browser.  The second parameter
        is the function within views.py which gets executed for that url.
        The third parameter is a name associated with the url which the html files use
        to identify a specific path.
"""

from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="Store-home"),
    path("view_category/<str:name>/", views.view_category, name="Store-view_category"),
    path("search_results", views.search_results, name="Store-search_results"),
    path("view_item/<str:name>/", views.view_item, name="Store-view_item"),
    path("view_cart/<str:name>", views.view_cart, name="Store-view_cart"),
    path("checkout", views.checkout, name="Store-checkout"),
    path("about", views.about, name="Store-about")
 ]