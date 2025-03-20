import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyA4ByLRJXvKVXlZdnT_9bRaaX1RAaq04DQ")

meal_combo = """

from itertools import combinations
import sqlite3

# Extract meal items and their prices from the provided meal_type string
meal_prices = {
    "Bread": 1500,
    "Akara(10)": 1000,
    "Moi-moi": 700,
    "Pap (corn)": 500,
    "Pap (millet)": 500,
    "Small Chops": 2500,
    "Jollof Rice": 1500,
    "Fried Rice": 1500,
    "White Rice": 3000,
    "Ofada Rice": 4000,
    "Spaghetti(Plain white)": 4000,
    "Spaghetti meal": 4000,
    "Indomie noodles (Plain white superpacks)": 1000,
    "Indomie noodles meal (1 superpacks)": 1000,
    "Egg (boiled)": 500,
    "Cooked Tilapia Fish": 3000,
    "Fried Titus Fish": 3000,
    "Roasted Tilapia Fish": 3000,
    "Stewed Cota Fish": 3000,
    "Dried Fish": 3000,
    "Peppered Panla Fish": 3000,
    "Smoked Fish": 3000,
    "Fried Cow meat": 3000,
    "Boiled Cow meat": 3000,
    "Peppered Cow meat": 3000,
    "Roasted Cow meat": 3000,
    "Fried Goat meat": 3000,
    "Boiled Goat meat": 3000,
    "Peppered Goat meat": 3000,
    "Roasted Goat meat": 3000,
    "Fried Ram meat": 3000,
    "Boiled Ram meat": 3000,
    "Peppered Ram meat": 3000,
    "Roasted Ram meat": 3000,
    "Fried Chicken": 3000,
    "Boiled Chicken": 3000,
    "Peppered Chicken": 3000,
    "Roasted Chicken": 3000,
    "Fried Chicken (Agric)": 3000,
    "Boiled Chicken (Agric)": 3000,
    "Peppered Chicken (Agric)": 3000,
    "Roasted Chicken (Agric)": 3000,
    "Eba": 700,
    "Fufu": 900,
    "Semovita": 900,
    "Semolina": 900,
    "Amala": 900,
    "Pounded Yam": 900,
    "Egusi Soup": 1000,
    "Ogbono Soup": 1000,
    "Efo Riro": 1600,
    "Stew": 1300,
    "Oha Soup": 1200,
    "Edikang Ikong Soup": 1000,
    "Egg Sauce": 1500,
    "Fish Sauce": 1000,
    "Ayamase Sauce": 4000,
    "Beans": 3000,
    "Boiled Yam": 3000,
    "Fried Yam": 1500,
    "Yam Porridge (Asaro)": 3500,
    "Boiled Sweet Potato": 3500,
    "Fried Sweet Potato": 3500,
    "Boiled Irish Potato": 3500,
    "Fried Irish Potato": 3500,
    "Boiled Plantain": 3000,
    "Fried Plantain": 3000,
    "Shawarma (Nigerian Style)": 3500,
    "Grilled Chicken with Fried Yam": 5000,
    "Bole & Fish Sauce": 3500,
    "Peppersoup Goat Meat": 4200,
    "Peppersoup Chicken": 4200,
    "Nkwobi": 4500,
    "Suya with Onions & Pepper": 3000,
    "Bottled Water": 300,
    "Orange Juice": 700,
    "Mango Juice": 700,
    "Punch": 300
}

db_path = "database.sqlite"

# Generate all possible meal combinations
meal_combinations = []
for r in range(1, 4):  # 1-item, 2-item, and 3-item combinations
    for combo in combinations(meal_prices.keys(), r):
        name = " and ".join(combo) if len(combo) == 2 else ", ".join(combo)
        price = sum(meal_prices[item] for item in combo)
        description = f"A combination of {name}."
        deleted = 0
        image = None
        meal_combinations.append((name, description, price, image, deleted))
        

# Insert into the SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Insert meal combinations into the products table
cursor.executemany("INSERT INTO products (name, description, price, image, deleted) VALUES (?, ?, ?, ?, ?)", meal_combinations)

# Commit changes and close connection
conn.commit()
conn.close()

# Output number of records inserted
len(meal_combinations)


"""

l = "Destination-route:Dawko MFM(Dwako, Abuja, Nigeria) JRJ Excellet academy(Aldenco Abuja, Nigeria) Time-frame: 8:00AM - 6:PM User Name: Mr. David Ope username: @david bright" 
m = "Destination-route: Library, senate-building Time-frame: 8:00AM - 6:PM User Name: Mr. David Ope User Number: 09044559334"

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content(f"write the most common complete group from these {l, m}, from the question only (no explanations just raw answers), I want to go to a place to read ")
prompt = "BEans and platain and bottle waterr i.e h2o . "
response2 = model.generate_content(f"Analyse and just return one products.name which is actually in the database if checked. No matter how much prompt in given, let it best match the real db. Based on the python file {meal_combo} how would a user who asked for the prompt: '{prompt}' interpret it in the database. Just 1 output, the name of products table (products.name) that best satisfies prompt")

print(response2.text)

# print(f"write the most common complete group from these {l, m}, from the question only (no explanations just raw answers), I want to go to a place to read ")