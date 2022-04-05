
from os import name
from classes.villain import User
import random

class Game:
    def __init__( self):
        # username1= input("Enter p1 name\n")
        # username2= input("Enter p2 name\n")
        self.p1= User.createplayer("p1") 
        self.p2= User.createplayer("p2")
        game_running=False
    


    def playgame(self):
        game_running=True
        turn= random.randint(1,4)
        
        while game_running:
            if turn%2==0:
                print(f"{self.p1.name} turn\n")
                self.p1.attack(self.p2)
                turn+=1
            else:
                print(f"{self.p2.name} turn\n")
                self.p2.attack(self.p1)
                turn+=1
            if self.p1.health <=0 or self.p2.health<=0:
                print("Game Over")
                if self.p1.health<=0:
                    print(f"{self.p1.name} wins")
                else:
                    print(f"{self.p2.name} wins")
                game_running=False
        return self
    
            
