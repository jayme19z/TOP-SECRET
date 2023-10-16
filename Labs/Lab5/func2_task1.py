# Write a function that takes a single movie and returns True if its IMDB score is above 5.5
def is_high_imdb_score(movie):
    return movie["imdb"] > 5.5

movie = {
    "name": "Usual Suspects",
    "imdb": 7.0,
    "category": "Thriller"
}

result = is_high_imdb_score(movie)
print(result)