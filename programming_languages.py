""" Lecture code example  """

languages = ['Python', 'Java', 'Javascript', 'c#', 'Swift']

for language in languages:
    print(language)                         # prints languages for language list

all_languages = ' <> '.join(languages)
print(all_languages)                        # prints all languages in languages separated by <> symbols

languages.sort()
print(languages)
                        # The output of these 2 look reversed to me. Is this printing accurately?
languages.reverse()
print(languages)
