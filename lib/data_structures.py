spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [food['name'] for food in spicy_foods]
    return names
    

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food['heat_level'] > 5]
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = food['heat_level']
        spicy_string = "🌶" * heat_level
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {spicy_string}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    spicy_food = [food for food in spicy_foods if food['cuisine'] == cuisine]
    return spicy_food[0]

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    sum = 0
    for food in spicy_foods:
        sum += food['heat_level']
    average = sum / len(spicy_foods)
    return average

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

