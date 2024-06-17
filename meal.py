# 22/05/24 A program read the meal.db  by Japser Guo

# imports
import sqlite3

user_input = '0'
food_id = '0'


def print_special_req(result):
    '''The code is too long so I replace them by this function'''
    db = sqlite3.connect('meal.db')
    print(" _______________________________________________________________")
    print(f"|{'name':<25} | {'price':<6} | {'types':<14}| GF  | Veg |")
    print("|__________________________|________|_______________|_____|_____|")
    for i in result:
        spe = 0
        cursor = db.cursor()
        query = f'select special_req_id from foods_spe_req where foods_spe_req.foods_id = {i[0]};'
        cursor.execute(query)
        special_req = cursor.fetchall()
        for s in special_req:
            if 1 in s:
                spe += 1
            elif 2 in s:
                spe += 2  # 0: none, 1: GF, 2: Veg, 3: both
        if spe == 1:
            print(f"|{i[1]:<25} | {i[2]:<6} | {i[3]:<14}| yes | no  |")
        elif spe == 2:
            print(f"|{i[1]:<25} | {i[2]:<6} | {i[3]:<14}| no  | yes |")
        elif spe == 3:
            print(f"|{i[1]:<25} | {i[2]:<6} | {i[3]:<14}| yes | yes |")
        else:
            print(f"|{i[1]:<25} | {i[2]:<6} | {i[3]:<14}| no  | no  |")
    print("|__________________________|________|_______________|_____|_____|")


def print_meals_by_price():
    '''This function is for print out meals order by price'''
    db = sqlite3.connect('meal.db')
    cursor = db.cursor()
    query = 'select foods.food_id,foods.food_name,foods.price,types.types_type from foods join types on foods.type = types.types_id order by foods.price;'
    cursor.execute(query)
    result = cursor.fetchall()
    print_special_req(result)
    db.close()  # close the DB that opened


def print_one_type_by_price(type):
    '''This function is for print out one type of the meals order by price'''
    db = sqlite3.connect('meal.db')
    cursor = db.cursor()
    query = f"select foods.food_id,foods.food_name,foods.price,types.types_type from foods join types on foods.type = types.types_id where type = {type} order by foods.price;"
    cursor.execute(query)
    result = cursor.fetchall()
    print_special_req(result)
    db.close()  # close the DB that opened


def print_meals_in_range(min, max):
    '''This function is for print out meals search by a price range'''
    db = sqlite3.connect('meal.db')
    cursor = db.cursor()
    query = f"select foods.food_id,foods.food_name,foods.price,types.types_type from foods join types on foods.type = types.types_id where price <= {max} and price >= {min} order by foods.price;"
    cursor.execute(query)
    result = cursor.fetchall()
    print_special_req(result)
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
