
print("-" *7, " GRADE GENERATOR", "-" *7, "\n")
print("# Python Skills Test\n")

#ask the users what is maximum score and how many points they received

maxScore = float(input("\nWhat is the maximum score of the test?\n"))

pointsReceived = float(input("\nHow many points did you receive?\n"))

#Figure out the percentage the user received and round to 2 decimal places.

percentage = (pointsReceived * 100) / maxScore
percentage = round(percentage, 2)

#Use if/elif statements to show users the letter grade they received.

print("\n")
print("-" * 7, "Your score", "-" * 7)
print("\nYou received ", int(pointsReceived), " points of ", int(maxScore), " maximum points, which is ", percentage, "% of the total test score.")




#At the end, the user should see the letter grade they received and the percentage correct.