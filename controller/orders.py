components = [
    {
        'name': 'screw',
        'price': 25
    },
    {
        'name': 'nut',
        'price': 14
    }
]

orders = [{
    'id': 1,
    'items': components,
    'total_price': 39,
    'state': 'finished'
}]


def add_order(data):
    print(data)
    try:
        order = {
            'id': data['id'],
            'items': data['items'],
            'state': 'start'
        }
        orders.append(order)
        return 200
    except:
        return None


def get_all_orders():
    return orders
