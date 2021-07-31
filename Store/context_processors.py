"""
    Author: Riley Radle
    Despcription:
        context_processors.py allows me to pass information to
        all of the templates in the project (essentially making
        that information global).  This allows me to display 
        categories in the navbar which exists in base.html
        (needed because base.html doesn't have a view in views.py
        through which to pass information).
"""

from .models import Category


"""
    Simple method to query the Categories from the database and return them
    @param request: a string representation of the request that is generated 
                    from the html pages
"""
def get_categories(request):
    return {
        "categories" : Category.objects.all()
    }