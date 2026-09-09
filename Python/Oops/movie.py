class Movie:
    title:str
    language:str
    year:int
    director:str
    genre:str

    def __init__(self,title,language,year,director,genre):

        self.title=title
        self.language=language
        self.year=year
        self.director=director
        self.genre=genre


    def get_movie(self):
        print(self.title,self.language,self.year,self.director,self.genre) 

movie1=Movie("Bangolore days","Malayalam",2014,"Anjali menon","Drama")
movie2=Movie("Kumbalangi Nights","Malayalam",2019,"Madhu C Narayanan","Drama")

movie1.get_movie()
movie2.get_movie()
