#22/05/24 A program read the meal.db  by Japser Guo

# imports
import sqlite3


def print_meals_by_price():
    db = sqlite3.connect('meal.db')
    cursor = db.cursor()
    cursor.execute('select foods.food_name,foods.price,special_reqs.req_name,types.types_type from foods join special_reqs on foods.special_req = special_reqs.req_id join types on foods.type = types.types_id order by foods.price;')
    result = cursor.fetchall()
    for i in result:
        print(f"|{i[0]:<25} | {i[1]:<6} | {i[2]:<15} | {i[3]:<14}|")
    db.close()  # close the DB that opened

print_meals_by_price()