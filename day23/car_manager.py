COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
import random
from turtle import Turtle


class CarManager:
    def __init__(self) -> None:
        self.cars = []
        self.distance = STARTING_MOVE_DISTANCE
        #self.create_cars()
    

    # def create_cars(self):
    #     shop = random.randint(0,len(COLORS))
    #     for item in range(shop):
    #         self.car()
        

    def car(self):
        random_choice = random.randint(1,6)
        if random_choice == 1:
            new_car = Turtle("square")
            new_car.shapesize(1,2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(300, random.randint(-270,260))
            self.cars.append(new_car)
        
    def levelup(self):
        self.distance += MOVE_INCREMENT


    def move_car(self):
        for item in self.cars:
            item.backward(self.distance)

    



        
    
        


        


    
