from mysql import connector


class IssuesListCreateRetrieveUpdateDestroy:

    def __init__(self, user=None, password=None):

        self.connection = connector.connect(
            user=user,
            password=password,
            host="localhost",
            database="road_issue_db"
        )

        self.cursor = self.connection.cursor()

    def post(self, **kwargs):

        query = """
        insert into issues(title, location, posted_by, status)
        values(%s, %s, %s, %s)
        """

        values = list(kwargs.values())

        self.cursor.execute(query, values)

        self.connection.commit()

        print("Issue Added")

    # list
    def get(self):

        query = "select * from issues"

        self.cursor.execute(query)

        record = self.cursor.fetchall()

        for issue in record:
            print(issue)

    
    def retrieve(self,id=None):

        query = "select * from issues where id=%s"

        values = (id,)

        self.cursor.execute(query, values)

        record = self.cursor.fetchone()

        print("retrieve=", record)


    def put(self, id=None, **kwargs):

        place_holder = ""

        for k in kwargs.keys():
            place_holder += k + "=%s,"

        place_holder = place_holder.rstrip(",")

        query = f"update issues set {place_holder} where id=%s"

        values = list(kwargs.values())

        values.append(id)

        self.cursor.execute(query, values)

        self.connection.commit()

        print("Record Updated....")


issue_instance = IssuesListCreateRetrieveUpdateDestroy(user="root",password="Password@123")

issue_instance.post(title="missing street light",location="tvm",posted_by="krishna",status="unsolved")

issue_instance.get()

issue_instance.retrieve(id=2)

issue_instance.put(id=3,title="road repaired",status="solved")