class FundWise:

    def __init__(self):

        self.expenses=[{
            "id":1,"title":"Food","amount":200,"category":"food","owner":"sooraj"                

        }]

    def post(self,**kwargs):

        self.expenses.append(kwargs)

        print("record has been created.....")

    def get(self):

        if len(self.expenses)==0:

            print("no records")

        else:

            for e in self.expenses:

                print(e) 

    def retrieve(self,id=None):

        expense=[e for e in self.expenses if e.get("id")==id][0]

        print(expense)

    def put(self,id=None,**kwargs):

        expense=[e for e in self.expenses if e.get("id")==id][0]

        expense.update(kwargs)

        print("record updated....")

        print(expense)

    def delete(self,id=None):

        expense=[e for e in self.expenses if e.get("id")==id][0]

        self.expenses.remove(expense)

        print("deleted....")

        self.get()

expense_instance=FundWise()   

expense_instance.post(id=2,title="traveling",amount=500,category="travel",owner="sooraj")

expense_instance.get()

expense_instance.retrieve(id=1)

expense_instance.put(id=2,title="bus traveling",amount=340)

expense_instance.delete(id=2)


            