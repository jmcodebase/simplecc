"""
Simple calorie counter
Run the command for each food item you have and it will return the calories for the day. 
It saves the calorie information
in .simplecc in your home directory.

to run: simplecc.py food quantity unit
example: simplecc.py ribeye 25 oz

I don't have Windows or Mac so I won't be testing on those platforms. 

You are expected to update the dictionary that contains food items. 
Consider modifying this to suit your own needs.

Author: Joe McGovern
Date:2023-12-20
"""

import os
import sys
from typing import List
from datetime import datetime
from pathlib import Path
import csv
#import fooditems

FOOD_ITEMS_LOC = ""
ENABLE_LOGGING = False
HISTORY_FILE = ""

"""
Logging function

 Parameters:
    msg (string): The message to get output.

"""
def output(msg :str):
    if ENABLE_LOGGING is True:
        print (msg)


def default_food_items() -> str:
    return """OZ=\"oz\"
G=\"grams\"
BAG=\"bag\"
CONTAINER=\"container\"
SLICE=\"slice\"

food_items={
    \"ribeye\":(OZ,200),
    \"sirloin\":(OZ,100)
    }"""

def make_folder(folder:str):
    if not os.path.exists(folder):
        output(f"making folder: {folder}")
        os.makedirs(folder)

def check_if_file_and_folder_exists():
    home_dir = os.path.expanduser("~")
    folder_name = ".simplecc"
    path = os.path.join(home_dir,folder_name)
    config_folder = home_dir+"/.config/simplecc/"
    output(config_folder)
    config_path = os.path.join(config_folder, "fooditems.py")

    make_folder(path)

    current_date = datetime.now()
    day = current_date.day
    month = current_date.month 
    year = current_date.year
    
    file_name = f"{day}{month}{year}.simplecc"

    global HISTORY_FILE
    HISTORY_FILE = f"{path}/{file_name}"

    output(HISTORY_FILE)
    if not os.path.exists(HISTORY_FILE):
        Path(HISTORY_FILE).touch()

    make_folder(config_folder)
    global FOOD_ITEMS_LOC;
    FOOD_ITEMS_LOC = config_path

    output(f"config_path: {config_path}, FOOD_ITEM_LOC: {FOOD_ITEMS_LOC}")
    if not os.path.exists(config_path):
        with open(config_path, 'w') as file:
                output(f"making {config_path}")
                file.write(default_food_items())

def parse_parameters() -> tuple[str,float,str]:
    length = len(sys.argv)
    if length not in(4,5):
        raise ValueError("Not enough parameters given. Use food item quanity.")

    food_item_parameter = sys.argv[1]
    quantity_parameter = sys.argv[2]
    unit_parameter = sys.argv[3]
 
    if length == 5 and sys.argv[4].upper() == "TRUE":
        global ENABLE_LOGGING
        ENABLE_LOGGING = True

    output(f"food_item: {food_item_parameter}, quantity: {quantity_parameter}, unit: {unit_parameter}, ENABLE_LOGGING {ENABLE_LOGGING}")
    return food_item_parameter,float(quantity_parameter),unit_parameter

def calculate_calories(quantity:float,calories_per_unit:float)->float:
    output(f"quantity:{quantity} calories per unit: {calories_per_unit}")
    return float(quantity)*float(calories_per_unit)

def load_food_items()->dict[str,tuple]:
    output(FOOD_ITEMS_LOC)
    exec(open(FOOD_ITEMS_LOC).read(), globals())
    output(food_items)
    return food_items

def find_item_in_food_items(item):
    item = item.lower()
    #if item in fooditems.food_items:
    fi = load_food_items()
    if item in fi:
        return_items = fi[item]
        output(return_items)
        return return_items
    else:
        print("Item not found in fooditems.py. Please add it and try again")
        sys.exit(1)

def get_previous_calories() -> float:
    previous_calories=0.0
    with open(HISTORY_FILE, 'r', newline='') as file:
        csv_reader=csv.reader(file)
        for row in csv_reader:
            previous_calories += float(row[-1])
    return previous_calories

def write_row(row: List[str]):
    with open(HISTORY_FILE, 'a', newline='') as file:
        csv_writer=csv.writer(file)
        csv_writer.writerow(row)

def add_to_history_and_print(food_item:str,quantity:float,unit:str,calories_per_unit:float):
    number_of_cals = calculate_calories(quantity,calories_per_unit)
    previous_calories = get_previous_calories()
    total_calories = 0.0
    new_row = [food_item,str(quantity),unit,str(number_of_cals)]
    
    total_calories = previous_calories+number_of_cals
    new_row[-1]=str(number_of_cals)
    write_row(new_row)    
    print(f"You have consumed {total_calories} calories today")

def main(food_item:str,quantity:float,unit:str):
    output("simple calorie counter.")
    food_items_unit,food_items_calories = find_item_in_food_items(food_item)
    
    add_to_history_and_print(food_item,quantity,unit,food_items_calories)    

    output(f"{food_items_unit},{food_items_calories}") 
    output("end")

if __name__ == "__main__":
    food_item,quantity,unit = parse_parameters()
    check_if_file_and_folder_exists()
    main(food_item,quantity,unit)
