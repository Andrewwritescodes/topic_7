""" Lecture code example  """

languages = ['Python', 'Java', 'Javascript', 'c#', 'Swift']

for language in languages:
    print(language)

# all_languages = ' <> '.join(languages)
# print(all_languages)

languages.sort()
print(languages)
                        # The output of these 2 look reversed to me. Is this printing accurately?
languages.reverse()
print(languages)
