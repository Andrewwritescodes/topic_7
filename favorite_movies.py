""" Lecture code project to sort favorite movies """

movies = ['The Matrix', 'Back To The Future', 'Space Jam', 'The Big Lebowski']
print(movies)                                                                   # prints list of movies as is

movies.sort()
print(movies)                                                                   # prints list of movies alphabetically

movies.reverse()
print(movies)                                                                   # prints list of movies is reverse alphabetical order

for movie in movies:
    print(movie)                                                                # for loop to print movies individually

all_movies = ' ~ '.join(movies)
print(all_movies)                                                               # prints all movies separated by ~ symbol

movies.append('Beetlejuice')
print(movies)
movies.append('Inception')
print(movies)
