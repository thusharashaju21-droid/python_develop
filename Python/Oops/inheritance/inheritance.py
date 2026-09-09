#child class access method and  properites of parent class => inheritance


class Parent:

    def house(self):
        print("parent class house method.....")

class Child(Parent): #inheritance

    def social_media_account(self):
        print("child class social media account......") 

child_instance = Child()

child_instance.social_media_account() 
child_instance.house()              
