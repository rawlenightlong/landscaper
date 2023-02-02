# Landscaper

## Game State
game = {"tool": 0, "money": 0}

tools = [
    {"name": "teeth", "profit" : 1, "cost": 0},
    {"name": "rusty scissors", "profit" : 5, "cost": 5},
    {"name": "old-timey push mower", "profit" : 50, "cost": 25},
    {"name": "battery-powered mower", "profit" : 100, "cost": 250},
    {"name": "team", "profit" : 250, "cost": 500},
    ]

# Game Option Functions

def cutGrass():
    tool = tools[game["tool"]]
    print(f'You cut the grass with your {tool["name"]} and make ${tool["profit"]}')
    game["money"] += tool["profit"]
    
def checkStats():
    tool = tools[game["tool"]]
    print(f'You have ${game["money"]} in your account and are using a {tool["name"]}')
    
def upgrade():
    nextTool = tools[game["tool"] + 1]
    if (nextTool == None):
        print("There are no more tools available")
        return 0
    if (game["money"] < nextTool["cost"]):
        print("Not enough money to buy tool!")
        return 0
    game["money"] -= nextTool["cost"]
    game["tool"]  += 1
    
def winCheck():
    if(game["tool"] == 4 and game["money" == 1000]):
        print("You Win!")
        return True
    return False
    
    
    
uinput = input("Welcome to Landscaper! Enter 'Start' to begin, enter 'Q' to Quit")


if (uinput == 'Start'):
    if (game["money"] < 5):
        print(f'You have ${game["money"]} in your account')
        workinput = input(f"You have")
    if (game["money"] < 25):
       print(f'You have ${game["money"]} in your account')
    if (game["money"] < 250):
        print(f'You have ${game["money"]} in your account')
    if (game["money"] < 500):
        print(f'You have ${game["money"]} in your account')
pass
    