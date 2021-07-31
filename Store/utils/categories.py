from ..models import Category

categories = []

def add_category(name, image):
    category = Category()
    category.name = name
    category.image = image

    # Add the category to the list
    categories.append(category)

# Portrait
add_category(
    "Portrait",
    "Store/images/categories/Portraits.jpg",
)

# Shirt
add_category(
    "Shirt",
    "Store/images/categories/Shirts.jpg",
)

# Shoe
add_category(
    "Shoe",
    "Store/images/categories/Shoes.jpg",
)

# Print
add_category(
    "Print",
    "Store/images/categories/Prints.jpg",
)


