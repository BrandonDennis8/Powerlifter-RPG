import time

SLEEP = 2

def getSpeed(obj):
    return obj.speed

def getCounter(obj):
    return obj.counter

def printNames(participants):
    print("\nOrder of queue:")
    order = 1
    for player in participants:
        print(f"{order}: {player.name}, C={player.counter}")
        order += 1
    print("")
    sleep()
    time.sleep(1)

def sleep():
    time.sleep(SLEEP)