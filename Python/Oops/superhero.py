class SuperHero:

    name:str
    power:str
    universe:str

    def __init__(self,name,power,universe):

        self.name=name
        self.power=power
        self.universe=universe

    def get_superhero(self):
        print(self.name,self.power,self.universe)

superhero1=SuperHero("spiderman","spreadweb","marvel")
superhero2=SuperHero("minnal murali","run","bj")  
superhero3=SuperHero("batman","fly","dc")

superhero1.get_superhero()
superhero2.get_superhero()
superhero3.get_superhero()
