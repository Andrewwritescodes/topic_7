""" Lecture code project to sort favorite movies """

import random

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
print(movies)                                                                   # prints movies list with Beetlejuice added at the end
movies.append('Inception')
print(movies)                                                                   # prints movies list with Inception added at the end

number_of_movies = len(movies)
print(f'There are {number_of_movies} movies in the movies list.')               # prints the amount of movies in the movies list including the appended additions

movies.remove('Space Jam')
print(movies)                                                                   # prints movies list without Space Jam

first_movie = movies.pop(0)
print(movies)                                                                   # prints movies list with pop function to remove item in index position 0
print(first_movie)                                                              # uses pop function to print only the first movie in the movies list

last_movie = movies.pop()
print(last_movie)                                                               # prints only last movie in movies list

movies.pop()
print(movies)                                                                   # prints movies list without last item in list due to empty pop function

random.shuffle(movies)                                                          # function to randomize order of movies in movies list

for index, movie in enumerate(movies):
    print(f'{index+1}: {movie}')                                                # for loop to print movies in movies list. this loop comes after the random.shuffle line, so movies will print in random order
