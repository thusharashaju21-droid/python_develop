#multiple inheritance- one child class inside two parent class

class Father:

    def cricket_skill(self):
        print("father cricket skill")

        
    def dancing_skill(self):
         print("father dancing skill")

class Mother:

     def dancing_skill(self):
         print("mother dancing skill")

class Child(Father,Mother):

    def coding_skill(self):
        print("child coding skill")

child_instance=Child()

child_instance.coding_skill()
child_instance.dancing_skill() #first(child)- parent class call
child_instance.cricket_skill()