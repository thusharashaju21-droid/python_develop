#event add,list,detail,update,delete

class EventWise:

    def __init__(self):

        self.programs=[
            {"id":1,"event":"group song","name":"sura","contact":7012219886,"batch":"generalist","faculty":"kunja"}

        ]

    def post(self,**kwargs):

        self.programs.append(kwargs)

        print("record has been created....")

    def get(self):

        if len(self.programs)==0:

            print("no records")

        else:

            for p in self.programs:
   
                print(p)  

    def retrieve(self,id=None):

        program=[p for p in self.programs if p.get("id")==id][0]

        print(program) 

    def put(self,id=None,**kwargs):

        program=[p for p in self.programs if p.get("id")==id][0]

        program.update(kwargs)

        print("record updated...")

        print(program)

    def  delete(self,id=None):

        program=[p for p in self.programs if p.get("id")==id][0]  

        self.programs.remove(program) 

        print("deleted...")

        self.get()
        

event_instance=EventWise()

event_instance.post(id=2,event="dance",contact="24473",batch="sura",faculty="abu")

event_instance.get()

event_instance.retrieve(id=1)

event_instance.put(id=2,name="kunja",contact="334456")

event_instance.delete(id=2)

