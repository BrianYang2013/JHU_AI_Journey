max_items_in_bag = 3

def shopping_bag_combinations(curr_bag, remaining_items):
    """
    Output every combination of items that fit
    in a shopping bag. Each recursive call moves
    one item into the shopping bag.
    """
    if len(curr_bag) == max_items_in_bag:
        # Base case: Shopping bag full
        bag_value = 0
        for item in curr_bag:
            bag_value += item['price']
            print(item['name'], ' ', end=' ')
        print('=', bag_value)
    else:
        # Recursive case: Move one of the remaining items
        # to the shopping bag.
        for index, item in enumerate(remaining_items):
            # Move item into bag
            curr_bag.append(item)
            remaining_items.pop(index)

            shopping_bag_combinations(curr_bag, remaining_items)

            # Take item out of bag
            remaining_items.insert(index, item)
            curr_bag.pop()

items = [
    {
        'name': 'Milk',
        'price': 1.25
    },
    {
        'name': 'Belt',
        'price': 23.55
    },
    {
        'name': 'Toys',
        'price': 19.05
    },
    {
        'name': 'Cups',
        'price': 11.85
    }
]

bag = []
shopping_bag_combinations(bag, items)