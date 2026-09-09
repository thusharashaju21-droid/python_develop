from mysql import connector


class ExpenseListCreateRetreieveUpdateDestroy:

    def __init__(self, user=None, password=None):

        self.connection = connector.connect(
            user=user,
            password=password,
            host="localhost",
            database="tripwise_db"
        )

        self.cursor = self.connection.cursor()

    # create
    def post(self, **kwargs):

        query = """
        insert into expense(trip, paid_by, amount, category)
        values(%s, %s, %s, %s)
        """

        values = list(kwargs.values())

        self.cursor.execute(query, values)

        self.connection.commit()

        print("Expense Added")

    # list
    def get(self):

        query = "select * from expense"

        self.cursor.execute(query)

        record = self.cursor.fetchall()

        for exp in record:
            print(exp)

    # retrieve
    def retrieve(self, id=None):

        query = "select * from expense where id=%s"

        values = (id,)

        self.cursor.execute(query, values)

        record = self.cursor.fetchone()

        print("retrieve=", record)

    # update
    def put(self, id=None, **kwargs):

        place_holder = ""

        for k in kwargs.keys():
            place_holder += k + "=%s," # like adding amount=%s

        place_holder = place_holder.rstrip(",")

        query = f"update expense set {place_holder} where id=%s"

        values = list(kwargs.values())

        values.append(id)

        self.cursor.execute(query, values)

        self.connection.commit()

        print("Record Updated....")


expense_instance = ExpenseListCreateRetreieveUpdateDestroy(
    user="root",
    password="Password@123"
)


# create
expense_instance.post(
    trip="munnar",
    paid_by="thushara",
    amount=6000,
    category="toll"
)


# list
expense_instance.get()


# retrieve
expense_instance.retrieve(id=2)


# update
expense_instance.put(
    id=2,
    amount=500,
    paid_by="sura",
    category="food"
)