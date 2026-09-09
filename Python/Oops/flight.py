class Flight:

    id:int
    name:str
    source: str
    destination:str
    ticket_price:float

    def __init__(self,id,name,source,destination,ticket_price):

        self.id=id
        self.name=name
        self.source=source
        self.destination=destination
        self.ticket_price=ticket_price

    def get_flight(self):

        print(self.id,self.name,self.source,self.destination,self.ticket_price)

flight1=Flight(1,"Emirates","Kochi","Uae",22000)
flight2=Flight(2,"Indigo","Kochi","Goa",7500)

flight1.get_flight()
flight2.get_flight()
