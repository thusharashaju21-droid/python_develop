class Train:

    id: int
    name: str
    source: str
    destination: str
    ticket_price: float

    def __init__(self, id, name, source, destination, ticket_price):

        self.id = id
        self.name = name
        self.source = source
        self.destination = destination
        self.ticket_price = ticket_price

    def get_train(self):

        print(self.id, self.name, self.source,
              self.destination, self.ticket_price)


train1 = Train(1, "Vande Bharat", "Ernakulam", "Bangolre", 1200)
train2 = Train(2, "Express", "Ernakulam", "Tvm", 1500)

train1.get_train()
train2.get_train()