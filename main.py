
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

if percentage > 100:
  print("\nSorry, you typed in something wrong.")
else:
  print("\nYou received", int(pointsReceived), "of", int(maxScore), "maximum points, which is", percentage, "% of the total score.\n")



if percentage >= 90 and percentage <= 100:
  print(percentage, "% gives you grade A+. It's the best possible score and you can't make it better. Well done!")
elif percentage >= 80 and percentage < 90:
  print(percentage, "% gives you grade A. Excellent!")
elif percentage >= 70 and percentage < 80:
  print(percentage, "% gives you grade B. It's pretty good. Keep going your hard work!")
elif percentage >= 60 and percentage < 70:
  print(percentage, "% gives you grade C. Not to bad, but you can do better. Try again!")
elif percentage >= 50 and percentage < 60:
  print(percentage, "% gives you grade D. It wasn't your best day, wasn't it? Give it a go one more time, we believe you can make it better.")
elif percentage < 50:
  print(percentage, "% gives you grade U, which means that you didn't meet the minimum requirements for passing. However, don't be discouraged. Use this setback as an opportunity to revise your knowledge and try again. We believe in you and are confident that you can improve and succeed.")




#At the end, the user should see the letter grade they received and the percentage correct.