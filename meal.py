# 22/05/24 A program read the meal.db  by Japser Guo


user_input = '0'
# imports
import sqlite3


def print_meals_by_price():
    db = sqlite3.connect('meal.db')
    cursor = db.cursor()
    cursor.execute('select foods.food_name,foods.price,special_reqs.req_name,types.types_type from foods join special_reqs on foods.special_req = special_reqs.req_id join types on foods.type = types.types_id order by foods.price;')
    result = cursor.fetchall()
    print(" __________________________________________________________________________")
    print(f"|{'name':<25} | {'price':<6} | {'special requirements':<20} | {'types':<14}|")
    for i in result:
        print(f"|{i[0]:<25} | {i[1]:<6} | {i[2]:<20} | {i[3]:<14}|")
    print("|__________________________|________|______________________|_______________|")
    db.close()  # close the DB that opened


def print_one_type_by_price(type):
    db = sqlite3.connect('meal.db')
    cursor = db.cursor()
    cursor.execute(f"select foods.food_name,foods.price,special_reqs.req_name,types.types_type from foods join special_reqs on foods.special_req = special_reqs.req_id join types on foods.type = types.types_id where type = {type} order by foods.price;")
    result = cursor.fetchall()
    print(" __________________________________________________________________________")
    print(f"|{'name':<25} | {'price':<6} | {'special requirements':<20} | {'types':<14}|")
    for i in result:
        print(f"|{i[0]:<25} | {i[1]:<6} | {i[2]:<20} | {i[3]:<14}|")
    print("|__________________________|________|______________________|_______________|")
    db.close()  # close the DB that opened


def print_meals_in_range(min,max):
    db = sqlite3.connect('meal.db')
    cursor = db.cursor()
    cursor.execute(f"select foods.food_name,foods.price,special_reqs.req_name,types.types_type from foods join special_reqs on foods.special_req = special_reqs.req_id join types on foods.type = types.types_id where price <= {max} and price >= {min} order by foods.price;")
    result = cursor.fetchall()
    print(" __________________________________________________________________________")
    print(f"|{'name':<25} | {'price':<6} | {'special requirements':<20} | {'types':<14}|")
    for i in result:
        print(f"|{i[0]:<25} | {i[1]:<6} | {i[2]:<20} | {i[3]:<14}|")
    print("|__________________________|________|______________________|_______________|")
    db.close()  # close the DB that opened


while True:
    if user_input == '3':
        break
    user_input = input("What do you want to do?\n1. print all meals\n2. print one type of meal\n3. exit program\n")
    if user_input == '1':
        print_meals_by_price()
    elif user_input == '2':
        while True:
            type = input("Please choose type:\n1. main course\n2. cold dish\n3. dessert\n4. drinks\n5. back\n6. exit program\n")
            if type == '5':  # 5. back
                break
            elif type == '6':  # 6. exit program
                user_input = '3'  # make user_input=3, so the progrm will quit
                break
            else:
                try:  # because there are int here, so we need a try
                    if 1 <= int(type) <= 4:  # check is the input a good value
                        print_one_type_by_price(type)
                    else:
                        print("That is not an option.")
                except ValueError:
                    print("That is not an option.")
    elif user_input == '3':
        break
    else:
        print("That is not an option.")
