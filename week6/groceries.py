def add_items(item, quantity, item_list = []): # Function has a default arg
    for existing_item in item_list:
        if existing_item[0] == item:
            existing_item[1] += quantity
            return item_list

    item_list.append([item, quantity]) # We don't create a new list here
    return  item_list

if __name__ == '__main__':
    item_list = [['organges', 10], ['coffee', 4], ['apples', 5], ['bread', 3]]

    add_items('coffee', 3, item_list) # add an item that already exists

    assert item_list[1][1] == 7

    add_items('chickens', 2, item_list) # add an item that does not exist

    assert item_list[4][0] == 'chickens' and item_list[4][1] == 2

    print('It works!')