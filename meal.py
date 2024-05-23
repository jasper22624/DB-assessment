# 22/05/24 A program read the meal.db  by Japser Guo

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


while True:
    user_input = input("What do you want to do?\n1. print all meals\n2. exit\n")
    if user_input == '1':
        print_meals_by_price()
    elif user_input == '2':
        type = input("choose type")
        print_one_type_by_price(type)
    elif user_input == '3':
        break
    else:
        print("That is not a option.")
