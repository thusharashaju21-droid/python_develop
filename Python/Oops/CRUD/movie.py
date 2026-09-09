#design and create a simple python crud application of movie each movie with attributes
# id,title,year,genre,rating,run_time,director

class MovieLens:

    def __init__(self):

        self.cinema=[
            {"id":1,"title":"bangolore days","year":2014,"genre":"drama","rating":9.3,"run_time":156,"director":"anjali menon"}
        ]

    def post(self,**kwargs):

        self.cinema.append(kwargs)

        print("movies added...")

    def get(self):

        if len(self.cinema)==0: 

            print("no record")

        else:

            for m in self.cinema:

                print(m)

    def retrieve(self,id=None):

        movies=[m for m in self.cinema if m.get("id")==id][0]

        print(movies)

    def put(self,id=None,**kwargs):

        movies=[m for m in self.cinema if m.get("id")==id][0]
                  
        movies.update(kwargs)

        print("movies updated...")

        print(movies)

    def  delete(self,id=None):
        
        movie=[m for m in self.cinema if m.get("id")==id][0]  
        
        self.cinema.remove(movie) 
        
        print(" movies deleted...")
        
        self.get()


movie_instance=MovieLens()

movie_instance.post(id=2,title="charile",year=2015,genre="thriller",rating=8.3,run_time=171,director="martin")

movie_instance.retrieve(id=1)

movie_instance.put(id=1,rating=9.0,director="Anjali Menon")

movie_instance.delete(id=2)





        




