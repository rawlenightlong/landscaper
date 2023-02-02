# Landscaper

## Game State
game = {"tool": 0, "money": 0}
money = 0
tools = [
    {"name": "teeth", "profit" : 1, "cost": 0},
    {"name": "rusty scissors", "profit" : 5, "cost": 5},
    {"name": "old-timey push mower", "profit" : 50, "cost": 25},
    {"name": "battery-powered mower", "profit" : 100, "cost": 250},
    {"name": "team", "profit" : 250, "cost": 500},
    ]
uinput = input("Welcome to Landscaper! Enter 'Start' to begin, enter 'Q' to Quit")

if (uinput == 'Start'):
    if (money < 5):
        print(f'You have ${money} in your account')
    if (money < 25):
       print(f'You have ${money} in your account')
    if (money < 250):
        print(f'You have ${money} in your account')
    if (money < 500):
        print(f'You have ${money} in your account')
pass
    