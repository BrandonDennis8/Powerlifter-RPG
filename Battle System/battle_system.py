PLAYER = 1
ENEMY = 2


USE_ITEM = 2
REG_ATTACK = 3
SPECIAL_ATTACK = 5
OVERDRIVE = 7



class playable:
    def __init__(self, Player, Name, Speed):
        self.player = Player
        self.name = Name
        self.speed = Speed

    counter = 0
    
def getSpeed(obj):
    return obj.speed
    
def playerAttack(player):
    print(f"{player.name}'s turn:\n  [1] Attack\n  [2] Item")
    choice = input()
    print(f"{player.name} Attacks!")
    player.counter += 3

def enemyAttack(enemy):
    print(f"{enemy.name}'s turn")
    print(f"{enemy.name} Attacks!")
    enemy.counter += 3


def startBattle(participants):
    # Sort priority queue initially by speed
    battleOver = False
    participants.sort(key= getSpeed, reverse=True)
    print("\n*** battle start ***")
    printNames(participants)
    
    while(battleOver == False):
        # Check if counter == 0 for any players/enemies
        for participant in participants:
            if(participant.counter == 0):
                # Check if enemy or player
                if(participant.player == PLAYER):
                    print(f"\nCounter before attack: {participant.counter}")
                    playerAttack(participant)
                    print(f"Counter after attack: {participant.counter}\n")
                elif(participant.player == ENEMY):
                    print(f"\nCounter before attack: {participant.counter}")
                    enemyAttack(participant)
                    print(f"Counter after attack: {participant.counter}\n")

        # Decrement all counters
        for participant in participants:
            participant.counter -= 1


def printNames(participants):
    for player in participants:
        print(player.name)
    
    
player1 = playable(PLAYER, "Platz", 11)
player2 = playable(PLAYER, "Maddox", 8)
player3 = playable(PLAYER, "Magnusson", 10)

enemy1 = playable(ENEMY, "WADA Employee 1 ", 12)
enemy2 = playable(ENEMY, "WADA Employee 2" , 7)

party = [player1,player2,player3,enemy1,enemy2]

print("*** before battle ***")
printNames(party)
startBattle(party)



print(player1.counter)


