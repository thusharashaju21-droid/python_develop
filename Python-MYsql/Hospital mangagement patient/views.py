from mysql import connector


class StockCreateListRetrieveUpdateDeleteFilterSummary:

    def __init__(self, user=None, password=None):

        if user == None or password == None:
            raise Exception("....Username and password required.....")

        self.connection = connector.connect(
            user=user,
            password=password,
            host="localhost",
            database="inventory_db"
        )

        self.cursor = self.connection.cursor()

    def post(self, **kwargs):

        db_col = (
            "item_name",
            "sku",
            "category",
            "quantity",
            "reorder_level",
            "unit_price",
            "storage_zone",
            "status"
        )

        difference = set(db_col).difference(kwargs.keys())

        if difference:
            raise Exception(f"....{difference} required...")

        col_str = ",".join(db_col)

        query = f"""
        insert into inventory
        ({col_str})
        values(%s,%s,%s,%s,%s,%s,%s,%s)
        """

        values = list(kwargs.values())

        self.cursor.execute(query, values)

        self.connection.commit()

        print("....record has been inserted ....")

    def get(self):

        query = "select * from inventory"

        self.cursor.execute(query)

        lst = self.cursor.fetchall()

        if lst:
            for l in lst:
                print(l)
        else:
            print("....no records found....")

    def retrieve(self, item_id=None):

        query = """
        select * from inventory
        where item_id=%s
        """

        values = (item_id,)

        self.cursor.execute(query, values)

        record = self.cursor.fetchone()

        if record:
            print(record)
        else:
            print("....record not found....")

    def put(self, item_id=None, **kwargs):

        place_holder = ""

        for k in kwargs.keys():
            place_holder += k + "=%s,"

        place_holder = place_holder.rstrip(",")

        query = f"""
        update inventory
        set {place_holder}
        where item_id=%s
        """

        values = list(kwargs.values())

        values.append(item_id)

        self.cursor.execute(query, values)

        self.connection.commit()

        print("....record has been updated....")

    def delete(self, item_id=None):

        query = """
        delete from inventory
        where item_id=%s
        """

        values = (item_id,)

        self.cursor.execute(query, values)

        self.connection.commit()

        print(".........record has been deleted.........")

    def filter(self, **kwargs):

        place_holder = ""

        for k in kwargs.keys():
            place_holder += k + "=%s and "

        place_holder = place_holder.rstrip("and ")

        query = f"""
        select * from inventory
        where {place_holder}
        """

        values = list(kwargs.values())

        self.cursor.execute(query, values)

        items = self.cursor.fetchall()

        if items:

            for p in items:
                print(p)

        else:
            print("...NO INVENTORY RECORDS...")

    def summary(self):

        query = """
        select category, sum(reorder_level) as total_order
        from inventory
        group by category
        """

        self.cursor.execute(query)

        record = self.cursor.fetchall()

        for r in record:
            print(r)


inventory = StockCreateListRetrieveUpdateDeleteFilterSummary(
    user="root",
    password="Password@123"
)


inventory.summary()


# inventory.filter(category="Bags")

# inventory.put(1, quantity=4, reorder_level=19)

# inventory.delete(6)

# inventory.get()

# inventory.retrieve(3)


# inventory.post(
#     item_name="Laptop Backpack",
#     sku="LB-BP-006",
#     category="Bags",
#     quantity=7,
#     reorder_level=12,
#     unit_price=1599.00,
#     storage_zone="Zone-C",
#     status="Low Stock"
# )


# inventory.post(
#     item_name="24 Inch LED Monitor",
#     sku="MN-LED-007",
#     category="Monitors",
#     quantity=20,
#     reorder_level=5,
#     unit_price=8999.00,
#     storage_zone="Zone-C",
#     status="In Stock"
# )


# inventory.post(
#     item_name="Wireless Keyboard",
#     sku="WK-KB-008",
#     category="Computer Accessories",
#     quantity=0,
#     reorder_level=10,
#     unit_price=1499.00,
#     storage_zone="Zone-A",
#     status="Out of Stock"
# )


# inventory.post(
#     item_name="Gaming Mouse Pad",
#     sku="GM-MP-009",
#     category="Gaming Accessories",
#     quantity=55,
#     reorder_level=15,
#     unit_price=799.00,
#     storage_zone="Zone-A",
#     status="In Stock"
# )


# inventory.post(
#     item_name="HDMI Cable 2 Meter",
#     sku="HD-HD-010",
#     category="Cables",
#     quantity=4,
#     reorder_level=10,
#     unit_price=599.00,
#     storage_zone="Zone-B",
#     status="Low Stock"
# )


# inventory.post(
#     item_name="Laptop Stand",
#     sku="LS-ST-011",
#     category="Computer Accessories",
#     quantity=25,
#     reorder_level=8,
#     unit_price=1899.00,
#     storage_zone="Zone-C",
#     status="In Stock"
# )