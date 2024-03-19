print()
print("           🍵 WELCOME TO COFFEE CLUB 🍵         ")
print('    ⁓⁓⁓ A coffee makes everything better ⁓⁓⁓         ')
print()
coffee_data = {
    'expresso': {
        'ingredients': {
            'water': 50,
            'coffee': 45,
        },
        'cost': 45
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24,
        },
        'cost' : 85,
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24
        },
        'cost': 100,
    },
    "black coffee": {
        'ingredients': {
            'water': 200,
            'coffee': 12
        },
        'cost': 30,
    }
}

profit = 0
resources = {
    'water': 1000,
    'milk': 750,
    'coffee': 800,
}

def res_suffi(inputs):
    for item in inputs:
        if inputs[item] >= resources[item]:
            print()
            print(f'SORRY, THERE IS NOT ENOUGH {item} ')
            print()
        return True

def coins():
    total = int(input('How many ₹2 coin? 🪙: '))*2
    total += int(input('How many ₹5 coin? 🪙: '))*5
    total += int(input('How many ₹10 coin? 🪙: '))*10
    total += int(input('How many ₹20 coin? 🪙: '))*20
    return total

def transaction(money_rec, drink_cost):
    if money_rec>=drink_cost:
        change=round(money_rec-drink_cost,2)
        print()
        print(f'HERE IS ₹{change} IN CHANGE 💵')
        print()
        global profit
        profit += drink_cost
        return True
    else:
        print()
        print(f"SORRY, YOU DON'T ENOUGH MONEY FOR {command} , MONEY REFUNDED ⇆  ")
        print()
        return False

def get_coffee(name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f'HERE IS YOUR {name} 🍵')
    print()
    print("        ⁓⁓⁓ ENJOY YOUR COFFEE ⁓⁓⁓ ")
    print()

on= True
while on:
    command = input('ENTER YOUR ITEM:')
    print()
    command = command.lower()
    if command=='off':
        on= False
    elif command == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Profit: ₹{profit}")
    else:
        drink = coffee_data[command]
        if res_suffi(drink['ingredients']):
            pay= coins()
            if transaction(pay,drink['cost']):
                get_coffee(command, drink['ingredients'])



