# 22/05/24 A program read the meal.db  by Japser Guo


user_input = '0'
# imports
import sqlite3


def print_meals_by_price():
    db = sqlite3.connect('meal.db')
    cursor = db.cursor()
    query = 'select foods.food_name,foods.price,types.types_type from foods join types on foods.type = types.types_id order by foods.price;'
    cursor.execute(query)
    result = cursor.fetchall()
    print(" ___________________________________________________")
    print(f"|{'name':<25} | {'price':<6} | {'types':<14}|")
    print("|__________________________|________|_______________|")
    for i in result:
        print(f"|{i[0]:<25} | {i[1]:<6} | {i[2]:<14}|")
    print("|__________________________|________|_______________|")
    db.close()  # close the DB that opened


def print_one_type_by_price(type):
    db = sqlite3.connect('meal.db')
    cursor = db.cursor()
    query = f"select foods.food_name,foods.price,types.types_type from foods join types on foods.type = types.types_id where type = {type} order by foods.price;"
    cursor.execute(query)
    result = cursor.fetchall()
    print(" ___________________________________________________")
    print(f"|{'name':<25} | {'price':<6} | {'types':<14}|")
    print("|__________________________|________|_______________|")
    for i in result:
        print(f"|{i[0]:<25} | {i[1]:<6} | {i[2]:<14}|")
    print("|__________________________|________|_______________|")
    db.close()  # close the DB that opened


def print_meals_in_range(min, max):
    db = sqlite3.connect('meal.db')
    cursor = db.cursor()
    query = f"select foods.food_name,foods.price,types.types_type from foods join types on foods.type = types.types_id where price <= {max} and price >= {min} order by foods.price;"
    cursor.execute(query)
    result = cursor.fetchall()
    print(" ___________________________________________________")
    print(f"|{'name':<25} | {'price':<6} | {'types':<14}|")
    print("|__________________________|________|_______________|")
    for i in result:
        print(f"|{i[0]:<25} | {i[1]:<6} | {i[2]:<14}|")
    print("|__________________________|________|_______________|")
    db.close()  # close the DB that opened


while True:
    if user_input == '4':
        break
    user_input = input("What do you want to do?\n1. print all meals\n2. print one type of meal\n3. search in price range\n4. exit program\n")
    if user_input == '1':
        print_meals_by_price()
    elif user_input == '2':
        while True:
            type = input("Please choose type:\n1. main course\n2. cold dish\n3. dessert\n4. drinks\n5. back\n6. exit program\n")
            if type == '5':  # 5. back
                break
            elif type == '6':  # 6. exit program
                user_input = '4'  # make user_input=4, so the progrm will quit
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
        min = input("enter the min price, or press enter to skip\n")
        max = input("enter the max price, or press enter to skip\n")
        if min == '':  # no input means skip so we need to set a range
            min = '0'
        if max == '':
            max = '1023'
        try:
            max = int(max)  # we need to turn it into int to compare
            min = int(min)
            if max <= min:  # max should be greater than min
                print("Price out of range.")
            elif min < 0 or min > 19:  # we don't have that expensive meals
                print("Price out of range.")
            else:
                print_meals_in_range(min, max)
        except ValueError:
            print("Invalid input.")
    elif user_input == '4':
        break
    else:
        print("That is not an option.")
