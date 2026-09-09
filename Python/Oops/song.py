class Song:

    id:int 
    movie_name:str
    title:str
    track_no:float
    singer:str
    duration:str

    def __init__(self,id,movie_name,title,track_no,singer,duration):

       self.id=id
       self.movie_name=movie_name
       self.title=title
       self.track_no=track_no
       self.singer=singer
       self.duration=duration

    def get_song(self):

        print(self.id,self.movie_name,self.title,self.track_no,self.singer,self.duration) 

song1=Song(1,"Bangolore Days","Aethu kari raavilum",1,"Haricharan","5:20")
song2=Song(2,"Mardona","Kaadhale",2,"Sruthy Sasidharan","3:25")

song1.get_song()
song2.get_song()
          

        