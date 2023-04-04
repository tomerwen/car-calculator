#!/usr/bin/python3
import random
import time
import boto3
import botocore
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
import car


Jaanukobil = car.Car.add_car("yes","111-11-111", "Tomer Wendel", 0 , 0)
Peachmobil = car.Car.add_car("yes",'222-22-222','Hodaya Cohen', 0,0)

def speedcalculator(car):
    while(car.running!='no'):
        car.speed = random.random()*200
        print(f'{car.number} speed is {str(car.speed)} km\h')
        car.km += car.speed/1800
        print(f'{car.number} milage is currently {car.km}km')
        car.running = input("Is the car still running?")
        time.sleep(2)
    print(f'Thank you {car.owner} for riding with us, in this ride you\'ve drove for {car.km} kilometers')
        
        
def pushToDB(car):
    print("Nothing")
    
        
# speedcalculator(Jaanukobil)
# speedcalculator(Peachmobil)

