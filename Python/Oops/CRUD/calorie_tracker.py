"""
#CRUD -create read update delete

Create = POST	(Add new food)
Read all =	GET	(Show all foods)
detailRead one =	RETRIEVE	(Show a specific food)
Update =	PUT	(Change food details)
Delete = DELETE	(Remove food)
"""
class DietLens:

    def __init__(self):

        self.food_logs = [
            {"id": 1, "name": "dosa", "calorie": 170, "owner": "hari"}
        ]

    def post(self, **kwargs): #add or create

        required_fields={"id","name","calorie","owner"} #set

        missing_fields=required_fields.difference(kwargs.keys())

        if missing_fields:

            raise ValueError(missing_fields,"is missing")
        
        #for field in required_fields:

        #    if field not in kwargs:

        #        raise ValueError(field,"is missing") 

        self.food_logs.append(kwargs)

        print("Record has been added.....")

    def get(self):  #list or all

        if len(self.food_logs)==0:

            print("no records found...")

        else:
        
         for log in self.food_logs:

            print(log)

    def retrieve(self,id=None):  #detail one

        if not id:

            raise ValueError("id missing")

        else:

            return [log for log in self.food_logs if log.get("id")==id] 
            

    def put(self,id=None,**kwargs):  #update
    #id missing 
    # #invalid id 
    # #fields    

        log = [ log for log in self.food_logs if log.get("id")==id] [0]
        log.update(kwargs)
        print("record has been updated..")
        print(log)

    def delete(self,id=None):   #remove

        log=[log for log in self.food_logs if log.get("id")==id][0]

        self.food_logs.remove(log)

        print("food log removed...")

        self.get()

            


diet_instance = DietLens()

diet_instance.post(id=2,name="idily",calorie=140,owner="vipin")
#diet_instance.post(id=3,name="uppumav",calorie=150)

diet_instance.get()

print(diet_instance.retrieve(id=1))

diet_instance.put(id=1,name="ghee roast",calorie=200)

diet_instance.delete(id=2)



