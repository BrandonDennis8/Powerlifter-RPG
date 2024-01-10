
from assist_functions import *
from battle_constants import *

class playable:
    def __init__(self, Player, Name, Speed, Overdrive):
        self.player = Player
        self.name = Name
        self.speed = Speed
        self.overdrive = Overdrive

    counter = 0
    
def playerAttack(player):
    print(f"\n{player.name}'s turn:\n  [1] Attack\n  [2] Item\n  [3] Overdrive")
    validInput = False

    while(validInput == False):
        validInput = True # avoid a bunch of break statements
        choice = input()

        match choice:
            case "1":
                print(f"{player.name} attacks!\n")
                player.counter += REG_ATTACK
            case "2":
                print(f"{player.name} used an item!\n")
                player.counter += USE_ITEM
            case "3":
                print(f"{player.name} used overdrive: {player.overdrive}!\n")
                player.counter += OVERDRIVE
            case _:
                print("incorrect action, try again")
                validInput = False
    sleep()

def enemyAttack(enemy):
    print(f"\n{enemy.name}'s turn")
    print(f"{enemy.name} attacks!\n")
    enemy.counter += REG_ATTACK
    sleep()


def startBattle(participants):
    # Sort priority queue initially by speed
    battleOver = False
    participants.sort(key= getSpeed, reverse=True)
    print("\n*** battle start ***")
    
    while(battleOver == False):
        # Print order of participants
        printNames(participants)

        # Check if counter == 0 for any players/enemies
        for participant in participants:
            if(participant.counter == 0):
                # Check if enemy or player
                if(participant.player == PLAYER):
                    # print(f"\nCounter before attack: {participant.counter}")
                    playerAttack(participant)
                    # print(f"Counter after attack: {participant.counter}\n")
                elif(participant.player == ENEMY):
                    # print(f"\nCounter before attack: {participant.counter}")
                    enemyAttack(participant)
                    # print(f"Counter after attack: {participant.counter}\n")

        # Decrement all counters
        for participant in participants:
            participant.counter -= 1    
        print("Counter decremented")
        participants.sort(key= getCounter)   
    
player1 = playable(PLAYER, "Platz", 11, "Quad Beam")
player2 = playable(PLAYER, "Maddox", 8, "Pec Slam")
player3 = playable(PLAYER, "Grigsby", 10, "Deadlift of Doom")

enemy1 = playable(ENEMY, "WADA Employee 1", 12, "n/a")
enemy2 = playable(ENEMY, "WADA Employee 2" , 7, "n/a")

party = [player1,player2,player3,enemy1,enemy2]

print("*** before battle ***")
printNames(party)
startBattle(party)



print(player1.counter)


