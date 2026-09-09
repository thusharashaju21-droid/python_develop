movies=[

    ["kgf","kannada",150,2005,8],
    ["balan","malayalam",130,2026,7],
    ["bangalore days","malayalam",150,2013,9],
    ["goatlife","malayalam",160,2024,9],
    ["abcd","malayalam",140,2008,6]
]

#display run_time ,year,rating of abcd
print(movies[3][2:])

#display all movie_titles
all_movies=[m[0]for m in movies]
print(all_movies)

#display all movie years
all_years={m[-2]for m in movies}
print(all_years)

#display all movie lanaguge
all_languages = [m[1] for m in movies]
print(all_languages)


