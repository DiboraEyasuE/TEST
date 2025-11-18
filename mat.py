import matplotlib.pyplot as plt
import numpy as np


# Simple line plot of temperature versus the days in a week
days = [1, 2, 3, 4, 5, 6, 7]
temperature = [72, 75, 68, 70, 74, 77, 71]

# Tips on plotting functionalities
# Colors: 'b'=blue, 'r'=red, 'g'=green, 'k'=black, etc.
# Line styles: '-'=solid, '--'=dashed, ':'=dotted, '-.'=dash-dot

plt.plot(days, temperature, color='k', marker='^', linestyle='--')
# You can use this format for a more readable code
# plt.plot(x, y, color='red', linestyle='--')
# you can put markers for critical points using shape letters after your color letter
# Common markers: 'o'=circle, 's'=square, '^'=triangle, 'D'=diamond, '.'=point
#'b' = blue, 'g' = green, 'r' = red, 'c' = cyan, 'm' = magenta,'y' = yellow,'k' = black, 'w' = white

plt.title("Weekly Temperature", fontsize=15, color='b')
plt.xlabel("Days of the week", fontsize=12, color='b')
plt.ylabel("Temperature(F)", fontsize=12, color='b')

# Tuples like this are possible too
# plt.plot(x, y, color=(1.0, 0.5, 0.0))  # orange

plt.show()

# Scattered plots

std = [1, 2, 3, 4, 5, 6, 7, 8]
score = [85, 92, 78, 65, 95, 88, 72, 90]
# to see only the scattered plot with markers, use this without the previous code
plt.scatter(std, score, color='k', marker="*")
plt.title("Student Scores")
plt.xlabel("Student id")
plt.ylabel("Scores")
plt.show()

# Bar graphs

# vertical bar graphs
subjects = ['Programming II', 'Algebra', 'Calculus', 'Statistics']
stars = [15, 30, 25, 20]

# plt.bar(fruits, quantities, hatch='/')   diagonal lines
# plt.bar(fruits, quantities, hatch='\\')   backslash lines
# plt.bar(fruits, quantities, hatch='x')    cross pattern

plt.bar(subjects, stars, color=['brown', 'gray', 'k', 'c'], width=0.4)
plt.title("Subjects and their Stars", fontsize=18, color='m')
plt.xlabel("Starred Subjects", fontsize=15, color='m')
plt.ylabel("Number of stars from students", fontsize=15, color='m')
plt.show()

# vertical bar graphs

# plt.barh(subjects, stars, color='k') 
# The h at the end of the word bar makes it horizontal

# Creating Histograms

Scores = [65, 72, 78, 85, 88, 92, 95, 72, 78, 85, 88, 92, 65, 72, 78, 85, 88, 92, 95, 100]
plt.hist(Scores, bins=5, color='c')
plt.title("Score Distribution", fontsize=18, color='brown')
plt.xlabel("Number of students", fontsize=15, color='brown')
plt.ylabel("Exam scores", fontsize=15, color='brown')
plt.show()

# Pie charts

time_spent = [3, 7, 10, 5, 12]
skills = ['pandas', 'matplotlib', 'OOP', 'numpy', 'Other']

plt.pie(time_spent, labels=skills, colors=['k', 'c', 'm', 'grey', 'w'])
plt.title("Time Spent for Skills")
plt.show()



