""" Quiz scores lecture code example """

quiz_scores = [8, 4, 10, 9, 7]                              # list of quiz scores

quiz = int(input('Which quiz did you retake? '))            # Asks user to input quiz number for quiz they retook
index = quiz - 1                                            # adjusts quiz index to count starting from 1 instead of 0, so position 0 in the index = quiz score 1
score = int(input('What was your score on that quiz? '))    # asks user to input modified quiz score

quiz_scores[index] = score                                  # changes the quiz_scores index using the index = quiz - 1 line to accurately change the users score on they test they retook in the final output

print(quiz_scores)                                          # prints quiz scores with modified quiz score for the quiz that was retaken
