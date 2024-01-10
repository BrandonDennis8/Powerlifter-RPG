USE_ITEM = 2
REG_ATTACK = 3
SPECIAL_ATTACK = 5
OVERDRIVE = 7

class playable:
    def __init__(self, n, s):
        self.name = n
        self.speed = s
    counter = 0
    
def getSpeed(obj):
    return obj.speed
    
    
def StartBattle(participants):
    participants.sort(key= getSpeed)
    print("Sorted:\n\n", participants)
    
print("Whatsup")
    
player1 = playable("Platz", 11)
player2 = playable("Maddox", 8)
player3 = playable("Magnusson", 10)

enemy4 = playable("WADA Employee 1", 7)
enemy5 = playable("WADA Employee 2", 7)

party = {player1,player2,player3,enemy1,enemy2}

print(party)
StartBattle(party)



print(player1.counter)


