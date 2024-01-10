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
    
def startBattle(participants):
    # Sort priority queue initially by speed
    participants.sort(key= getSpeed, reverse=True)
    print("\n*** battle start ***")
    printNames(participants)
    
    # Check if counter == 0 for any players/enemies
    for participant in participants:
        if(participant.counter == 0):
            # Check if enemy or player
            if(participants[0].player == True):
                # Make attack selection
                pass
            else:
                # Enemy attack
                pass

    # Decrement all counters
    for participant in participants:
        participant.counter -= 1


def printNames(participants):
    for player in participants:
        print(player.name)
    
    
player1 = playable(PLAYER, "Platz", 11)
player2 = playable(PLAYER, "Maddox", 8)
player3 = playable(PLAYER, "Magnusson", 10)

enemy1 = playable(ENEMY, "WADA Employee 1 ", 7)
enemy2 = playable(ENEMY, "WADA Employee 2" , 7)

party = [player1,player2,player3,enemy1,enemy2]

print("*** before battle ***")
printNames(party)
startBattle(party)



print(player1.counter)


