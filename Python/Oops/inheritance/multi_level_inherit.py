#multi level inheritance

class Grandparent:

    def properties(self):
        print("2 acre land")

class Parent(Grandparent):

    def house(self):
        print("1500sqft house")

class Child(Parent):

    def social_media_account(self):
        print("social media account")

child_instance=Child()

child_instance.social_media_account()
child_instance.house()
child_instance.properties()

