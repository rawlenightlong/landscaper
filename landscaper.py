# Landscaper

## Game State
game = {"tool": 0, "money": 0}

tools = [
    {"name": "set of teeth", "profit" : 1, "cost": 0},
    {"name": "pair of rusty scissors", "profit" : 5, "cost": 5},
    {"name": "old-timey push mower", "profit" : 50, "cost": 25},
    {"name": "battery-powered mower", "profit" : 100, "cost": 250},
    {"name": "team of starved college kids", "profit" : 250, "cost": 500},
    ]

# Game Option Functions

def cutGrass():
    tool = tools[game["tool"]]
    print(f'You cut the grass with your {tool["name"]} and make ${tool["profit"]}')
    game["money"] += tool["profit"]
    print(f"You have ${game['money']}")
    
def checkStats():
    tool = tools[game["tool"]]
    print(f'You have ${game["money"]} in your account and are using the {tool["name"]}')
    
def upgrade():
    
    if (game['tool'] == 4):
        print("There are no more tools available!")
        return 0
    nextTool = tools[game["tool"] + 1]
    if (game["money"] < nextTool["cost"]):
        print(f"Not enough money to buy the {nextTool['name']} !")
        return 0
    game["money"] -= nextTool["cost"]
    game["tool"]  += 1
    print(f"You bought the {nextTool['name']} for ${nextTool['cost']}! You now have ${game['money']}!") 
    if(game['tool'] == 4):
        print("There are no more tools to buy!")
    else:
        print(f"Your next tool is the {tools[game['tool'] + 1]['name']} and costs ${tools[game['tool'] + 1]['cost']}!")
    
def winCheck():
    if(game["tool"] == 4 and game["money"] >= 1000):
        print("You Win!")
        return True
    return False

print("Welcome to Landscaper! Pick an option:")    
while(True):
    
    i = input(" [1] Cut Grass [2] Check Stats [3] Upgrade [4] Quit") 
    i = int(i)
    
    if (i == 1):
        cutGrass()
    if (i == 2):
        checkStats()
    if (i == 3):
        upgrade()
    if (i == 4):
        print("You quit the game")
        break
    if (winCheck()):
        break


    

    