from csv import DictReader

fr = open("Python\\File Operation\\movies.csv", "r", encoding="UTF-8")

movies = list(DictReader(fr))   # list of dictionaries

unique_title = {p.get("Title") for p in movies}

print(unique_title)

