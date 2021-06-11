carts = [
    {
        "id": 0,
        "items": [
            {
                'name': 'screw',
                'price': 25
            },
            {
                'name': 'nut',
                'price': 14
            }
        ]
    }
]


def create_cart():
    id = len(carts)
    cart = {
        "id": id,
        "items": []
    }
    carts.append(cart)
    return cart


def get_cart(cart_id):
    for cart in carts:
        if cart["id"] == int(cart_id):
            return cart
    return None


def put_item_to_cart(cart_id, item):
    return ""


def __calculate_total_price__(cart):
    price = 0
    for el in cart["items"]:
        price += el["price"]
    return price
