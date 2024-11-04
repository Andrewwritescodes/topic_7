""""""

quiz_scores = [0] * 5
print(quiz_scores)

for quiz, score in enumerate(quiz_scores):
    new_score = int(input(f'Enter score for quiz {quiz+1}: '))
    quiz_scores[quiz] = new_score

print('Your scores are: ')
print(quiz_scores)
