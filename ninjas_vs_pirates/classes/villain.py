import random
class User:

    def __init__( self , name ):
        self.name = name
        self.strength = 25
        self.health = 100 
        self.defense=10

    @classmethod
    def createplayer(cls,name):
        userinput=input(f"Enter {name} name\n")
        return cls(userinput)

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nDefense: {self.defense}\nHealth: {self.health}\n")
    
    def change_health(self, amount):
        self.health+= amount
        return self.health

    def defend( self, opponent):
        opponent.defense = random.randint(5,opponent.defense)
        return opponent.defense

    def attack ( self , opponent ):
        amount= random.randint(7,self.strength)
        print("Your attack is", amount)
        # print("Defense is", self.defend())
        print("Opponent defense was", opponent.defend(opponent))
        damage = amount-opponent.defense
        if(damage <= 0):
            print("Amount is", damage)
            print("Opponent defended\n")
        else:
            print("Attack damage was" ,damage,"\n")
            opponent.change_health(-damage)
        
        return self

    






