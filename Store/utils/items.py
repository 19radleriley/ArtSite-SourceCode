from ..models import Item, Category

items = []

def add_item(name, image, description, price, category, tags):
    item = Item()
    item.name = name
    item.image = image
    item.description = description
    item.price = price
    item.category = category
    item.tags = tags

    # Add the item into the list
    items.append(item)

# =========== Portraits ===========
portraits = Category.objects.get(name="Portrait")

# 1
add_item(
    "Realistic Graphite Drawing",
    "Store/images/items/rPortrait.jpg",
    [
        "Hand-Drawn Realistic Portrait",
        "Graphite and Charcoal",
        "8.5\" x 11\"",
        "Frame Included",
        "Submit your photo with your order",
    ],
    100.00,
    portraits,
    "realistic graphite drawings real black and white self portraits art",
)

# 2
add_item(
    "Personal Caricature",
    "Store/images/items/cPortrait.jpg",
    [
        "Digitally Drawn Cartoon Caricature",
        "Made with Adobe Photoshop and Illustrator",
        "8.5\" x 11\"",
        "Frame Included",
        "Submit your photo with your order",
    ],
    60.00,
    portraits,
    "personal caricatures cartoon funny self portraits drawings art",
)

# 3
add_item(
    "Harry Potter-ify Yourself",
    "Store/images/items/hpPortrait.jpg",
    [
        "I will draw you as if you were a Harry Potter character",
        "Digitally Drawn",
        "Made with Adobe Photoshop and Illustrator",
        "8.5\" x 11\"",
        "Frame Included",
        "Submit your photo, and other details you would like me to add, with your order",
    ],
    80.00,
    portraits,
    "harry potter style portraits drawings style cartoons funny fantasy art",
)

# 4
add_item(
    "Avatar-ify Yourself",
    "Store/images/items/atlaPortrait.jpg",
    [
        "I will draw you as if you were an Avatar the Last Airbender character",
        "Digitally Drawn",
        "Made with Adobe Photoshop and Illustrator",
        "8.5\" x 11\"",
        "Frame Included",
        "Submit your photo, and other details you would like me to add, with your order",
    ],
    80.00,
    portraits,
    "avatar style portraits self drawings cartoons nickelodeon kids funny fantasy art",
)

# 5
add_item(
    "Become a Super-Hero",
    "Store/images/items/sPortrait.jpg",
    [
        "I will draw you as if you as if you were a super-hero",
        "Digitally Drawn",
        "Made with Adobe Photoshop and Illustrator",
        "8.5\" x 11\"",
        "Frame Included",
        "Submit your photo, and details about your super-hero with your order",
    ],
    80.00,
    portraits,
    "super hero style portraits self comic drawing fantasy art"
)


# =========== Prints =========== 
prints = Category.objects.get(name="Print")

# 1
add_item(
    "Past Four Avatars",
    "Store/images/items/atlaPrint.jpg",
    [
        "Canvas print of the last four Avatars from the Avatar Universe",
        "Digitally Printed",
        "Design made with Adobe Photoshop and Illustrator",
        "24\" x 16\"",
        "Frame Included",
    ],
    50.00,
    prints,
    "past four avatars prints canvases drawings paintings wall art nickelodeon" + 
    "last airbender",
)

# 2
add_item(
    "Miles Graffiti",
    "Store/images/items/mmPrint.jpg",
    [
        "Canvas print of Miles Morales sitting in front of his art",
        "Digitally Printed",
        "Design made with Adobe Photoshop and Illustrator",
        "24\" x 16\"",
        "Frame Included",
    ],
    50.00,
    prints,
    "miles graffiti prints canvases drawings paintings wall art spider man super heros",
)

# 3
add_item(
    "Custom Wall Art",
    "Store/images/items/cPrint.jpg",
    [
        "Canvas print with your own custom image",
        "Digitally printed",
        "Design made with Adobe Photoshop and Illustrator",
        "24\" x 16\"",
        "Frame Included",
        "Submit your photo (or description) with your order",
    ],
    60.00,
    prints,
    "custom wall art submit picture canvases prints paintings drawings",
)

# 4
add_item(
    "Wizarding World Symbols",
    "Store/images/items/hpPrint.jpg",
    [
        "Canvas print of common symbols from the world of Harry Potter",
        "Digitally Printed",
        "Design made with Adobe Photoshop and Illustrator",
        "24\" x 16\"",
        "Frame Included",
        "Choose from one of several designs",
    ],
    50.00,
    prints,
    "wizarding world symbols prints canvases paintings harry potter wall art nine three quarters",
)

# 5
add_item(
    "The GOAT",
    "Store/images/items/mjPrint.jpg",
    [
        "Canvas print of Michael Jordn's famous free throw line dunk",
        "Digitally Printed",
        "Design made with Adobe Photoshop and Illustrator",
        "24\" x 16\"",
        "Frame Included",
    ],
    50.00,
    prints,
    "the goat canvas prints wall art paintings michael jordan mj bulls basketball sports",
)


# =========== Shirts =========== 
shirts = Category.objects.get(name="Shirt")

# 1
add_item(
    "Aang Learns Earth Bending",
    "Store/images/items/atlaShirt.jpg",
    [
        "Shirt with the character Aang from Avatar the Last Airbender",
        "Hand Pressed, Quality Guaranteed",
        "Design made with Adobe Photoshop and Illustrator",
        "Small, Medium, Large, X-Large",
    ],
    30.00,
    shirts,
    "aang learns earth bending avatar the last airbender shirts clothes nickelodeon",
)

# 2
add_item(
    "Platform Nine and Three Quarters",
    "Store/images/items/hpShirt.jpg",
    [
        "Shirt with the famous \"Platform 9 3/4\" from Harry Potter",
        "Hand Pressed, Quality Guaranteed",
        "Design made with Adobe Photoshop and Illustrator",
        "Small, Medium, Large, X-Large",
    ],
    30.00,
    shirts,
    "platform nine and three quarters 9 3/4 shirts harry potter clothes fantasy",
)

# 3
add_item(
    "Vintage Kobe Bryant",
    "Store/images/items/kbShirt.jpg",
    [
        "Shirt with several iconic photos of Kobe Bryant",
        "Hand Pressed, Quality Guaranteed",
        "Design made with Adobe Photoshop and Illustrator",
        "Small, Medium, Large, X-Large",
    ],
    30.00,
    shirts,
    "vintage kobe bryant kb rip black mamba basketball sports shirts clothes",
)

# 4
add_item(
    "Leap of Faith",
    "Store/images/items/mmShirt.jpg",
    [
        "Shirt of Miles Morales from the Leap of Faith scene in Into the Spider-Verse",
        "Hand Pressed, Quality Guaranteed",
        "Design made with Adobe Photoshop and Illustrator",
        "Small, Medium, Large, X-Large",
    ],
    30.00,
    shirts,
    "leap of faith shirts miles morales spider man super heros clothes",
)

# 5
add_item(
    "Vintage Space Jam",
    "Store/images/items/sjShirt.jpg",
    [
        "Shirt of the Looney Tunes characters from the original Space Jam movie",
        "Hand Pressed, Quality Guaranteed",
        "Design made with Adobe Photoshop and Illustrator",
        "Small, Medium, Large, X-Large",
    ],
    30.00,
    shirts,
    "vintage space jam basketball sports looney tunes cartoons shirts clothes",
)
  

# =========== Shoes =========== 
shoes = Category.objects.get(name="Shoe")

# 1
add_item(
    "ATLA Air Forces",
    "Store/images/items/atlaAF1.jpg",
    [
        "Hand painted Nike Air Force 1's",
        "Custom Avatar the Last Airbender Design",
        "High Quality Leather Paint",
        "Include your shoe size and any other details with your order"
    ],
    150.00,
    shoes,
    "atla air forces avatar last airbender shoes nike clothes custom painted nickelodeon",
)

# 2
add_item(
    "Cartoon Air Forces",
    "Store/images/items/cAF1.jpg",
    [
        "Hand painted Nike Air Force 1's",
        "Custom \"Cartoon\" Design",
        "High Quality Leather Paint",
        "Include your shoe size and any other details with your order"
    ],
    150.00,
    shoes,
    "cartoon air forces shoes clothes custom painted nike",
)

# 3
add_item(
    "Rick and Morty Air Forces",
    "Store/images/items/ramAF1.jpg",
    [
        "Hand painted Nike Air Force 1's",
        "Custom Rick and Morty Design",
        "High Quality Leather Paint",
        "Include your shoe size and any other details with your order"
    ],
    150.00,
    shoes,
    "rick and morty air forces shoes cothes custom painted nike",
)

# 4
add_item(
    "Harry Potter Air Forces",
    "Store/images/items/hpAF1.jpg",
    [
        "Hand painted Nike Air Force 1's",
        "Custom Harry Potter Design",
        "High Quality Leather Paint",
        "Include your shoe size and any other details with your order"
    ],
    150.00,
    shoes,
    "harry potter air forces shoes clothes custom painted nike fantasy",
)

# 5
add_item(
    "Spiderman Air Forces",
    "Store/images/items/smAF1.jpg",
    [
        "Hand painted Nike Air Force 1's",
        "Custom Spider-Man Design",
        "High Quality Leather Paint",
        "Include your shoe size and any other details with your order"
    ],
    150.00,
    shoes,
    "spiderman air forces shoes clothes super heros custom painted nike",
)
