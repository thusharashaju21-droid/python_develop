from mysql import connector


class TicketCreateListRetrieveUpdateDelete:

    def __init__(self, user=None, password=None):

        if user == None or password == None:
            raise Exception("Username and Password required")

        self.connection = connector.connect(
            user=user,
            password=password,
            host="localhost",
            database="customer_support_db"
        )

        self.cursor = self.connection.cursor()

    def post(self, **kwargs):

        db_cols = (
            "customername",
            "email",
            "subject",
            "description",
            "category",
            "priority",
            "status",
            "assigned_to"
        )

        difference = set(db_cols).difference(kwargs.keys())

        if difference:
            raise Exception(f"{difference} required")

        col_str = ",".join(db_cols)

        query = f"""
        insert into support_ticket({col_str})
        values(%s,%s,%s,%s,%s,%s,%s,%s)
        """

        values = list(kwargs.values())

        self.cursor.execute(query, values)

        self.connection.commit()

        print("Ticket Added")

    def get(self):

        query = """
        select * from support_ticket
        """

        self.cursor.execute(query)

        record = self.cursor.fetchall()

        for ticket in record:
            print(ticket)

    def retrieve(self, id=None):

        query = """
        select * from support_ticket where id=%s
        """

        values = (id,)

        self.cursor.execute(query, values)

        record = self.cursor.fetchone()

        print("retrieve =", record)

    def put(self, id=None, **kwargs):

        place_holder = ""

        for k in kwargs.keys():
            place_holder += k + "=%s,"

        place_holder = place_holder.rstrip(",")

        query = f"""update support_ticket set {place_holder} where id=%s"""

        values = list(kwargs.values())

        values.append(id)

        self.cursor.execute(query, values)

        self.connection.commit()

        print("Record Updated....")

    def filter(self, **kwargs):

        place_holder = ""

        for k in kwargs.keys():
            place_holder += k + "=%s and "

        place_holder = place_holder.rstrip("and ")

        query = f"""select * from support_ticket where {place_holder}"""

        values = list(kwargs.values())

        self.cursor.execute(query, values)

        record = self.cursor.fetchall()

        if record:

            for ticket in record:
                print(ticket)

        else:

            print("No records")

    def delete(self, id=None):

        query = """delete from support_ticket where id=%s"""

        values = (id,)

        self.cursor.execute(query, values)

        self.connection.commit()

        print("Ticket Deleted")
    def summary(self):

        query = """
        select status, count(*) 
        from support_ticket 
        group by status
        """

        self.cursor.execute(query)

        response = self.cursor.fetchall()

        priority_summary_query = """
        select priority, count(*) as count
        from support_ticket
        group by priority
        """

        self.cursor.execute(priority_summary_query)

        priority_summary = self.cursor.fetchall()

        print("priority summary=", priority_summary)

        print("summary=", response)

ticket_instance = TicketCreateListRetrieveUpdateDelete(user="root",password="Password@123")
ticket_instance.post(
    customername="Arun",
    email="Arun@gmail.com",
    subject="delivery issue",
    description="order has not arrived yet",
    category="delivery",
    priority="high",
    status="open",
    assigned_to="Anagha"
)
ticket_instance.get()


ticket_instance.retrieve(1)


ticket_instance.put(1,priority="low",status="resolved")


ticket_instance.filter(priority="high",status="open")


ticket_instance.summary()