favorite_movies = [
    "She's the Man",
    "Finding Nemo",
    "The Princess Diaries",
    "Shrek",
]
y = enumerate(favorite_movies)

movie_list = list(y)
# Learned how to print on multiple lines from claude
# This was to stop to many characters on a single line
print(
    f"Movie One: {movie_list[0][1]}, "
    f"Movie Two: {movie_list[1][1]}, "
    f"Movie Three: {movie_list[2][1]}, "
    f"Movie Four: {movie_list[3][1]}"
)
