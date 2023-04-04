import random
import time
class car:
    def __init__(self,running , number, owner, speed, km):
        self.running = True
        self.number = number
        self.owner = owner
        self.speed = speed
        self.km = km
        
        
Jaanukobil = car("yes","111-11-111", "Tomer Wendel", 0 , 0)

def speedcalculator(car):
    while(car.running!='no'):
        car.speed = random.random()*200
        print(f'{car.number} speed is {str(car.speed)} km\h')
        car.km += car.speed/1800
        print(f'{car.number} milage is currently {car.km}km')
        car.running = input("Is the car still running?")
        time.sleep(2)
        
        
def pushToDB(car):
    print("Nothing")
    
        
speedcalculator(Jaanukobil)