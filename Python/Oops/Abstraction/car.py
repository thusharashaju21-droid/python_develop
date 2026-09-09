from abc import ABC,abstractmethod
class Car(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Glanza(Car):

    def start(self):
        print("Glanza Start....") 

    def accelerate(self):
        print("Glanza car accelerate....")

    def stop(self):
        print("Glanza stoped.....")

glanza_instance= Glanza()

glanza_instance.start()
glanza_instance.accelerate()
glanza_instance.stop()