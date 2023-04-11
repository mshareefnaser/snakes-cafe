def print_menu():
    print('**************************************\n** Welcome to the Snakes Cafe! **\n')
    print('** Please see our menu below **\n**')
    print('** To quit at any time, type "quit" **\n**************************************\n')
    print('Appetizers\n----------\nWings\nCookies\nSpring Rolls\n')
    print('Entrees\n-------\nSalmon\nSteak\nMeat Tornado\nA Literal Garden\n')
    print('Desserts\n--------\nIce Cream\nCake\nPie\n')
    print('Drinks\n------\nCoffee\nTea\nUnicorn Tears\n')
    print('***********************************\n** What would you like to order? **\n***********************************\n')

def print_order():
    order = ''
    menu = ['Wings', 'Cookies', 'Spring Rolls', 'Salmon', 'Steak', 'Meat Tornado',
    'A Literal Garden', 'Ice Cream', 'Cake', 'Pie', 'Coffee', 'Tea', 'Unicorn Tears']
    orders_number = 0
    order_items = []
    unique_items=[]
    while order != 'quit':
        order = input('>')
        if order in menu:
            orders_number += 1
            if order in order_items:
                order_items.append(order)
                order_count = order_items.count(order)
                print("** {} orders of {} have been added to your meal **".format(order_count, order))
            else:
                order_items.append(order)
                print("** 1 order of {} have been added to your meal **".format(order))
        else:
            print ("Your order not listed in the menu, please choose one from it! ")    
    unique_items = list(set(order_items)) 
    if len(unique_items)>0:
        print ('** Your order details: **')   
        for item in order_items:
            if item not in unique_items:
                unique_items.append(item)
        for unique in unique_items:
            unique_counter=order_items.count(unique)
            print ("** {} of {} was added **".format (unique_counter,unique))
        print('** Thank you for visiting us **')
    else: 
        print ("** You didn't order anything ! **")

print_menu()
print_order()