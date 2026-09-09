class Book:
    title:str
    price:float
    author:str
    pages:int

    def set_book(self,title,price,author,pages):
        self.title=title
        self.price=price
        self.author=author
        self.pages=pages

    def get_book(self):
        print(self.title,self.price,self.author,self.pages)

Frankenstein=Book()
Kill_a_Mockingbird = Book()   
LeeMoby_Dick = Book() 
Kill_a_Mockingbird.set_book("Kill a Mockingbird",450,"Harper",345)        
Kill_a_Mockingbird.get_book()