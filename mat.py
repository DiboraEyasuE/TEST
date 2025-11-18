import matplotlib.pyplot as plt
import numpy as np


# Simple line plot of temperature versus the days in a week
days = [1, 2, 3, 4, 5, 6, 7]
temperature = [72, 75, 68, 70, 74, 77, 71]

# Tips on plotting functionalities
# Colors: 'b'=blue, 'r'=red, 'g'=green, 'k'=black, etc.
# Line styles: '-'=solid, '--'=dashed, ':'=dotted, '-.'=dash-dot

plt.plot(days, temperature, 'k^:')
# You can use this format for a more readable code
# plt.plot(x, y, color='red', linestyle='--')
# you can put markers for critical points using shape letters after your color letter
# Common markers: 'o'=circle, 's'=square, '^'=triangle, 'D'=diamond, '.'=point

plt.title("Weekly Temperature", fontsize=15, color='b')
plt.xlabel("Days of the week", fontsize=12, color='b')
plt.ylabel("Temperature(F)", fontsize=12, color='b')

# Don't be bothered about the many comments in the code 
# am deliberately doing this to use it as a cheatsheet too, brilliant ha😉😉
# I like being funny and creative while coding hope you'll like it too
# and guess what, I wanted to write a journal daily and be active on github so many times 
# but failed to do so because lack of discipline, you know inconsistency is a powerful disease
# so am gonna try to achieve both plans by creating a website to commit on precise daily messages
# for your information I don't have experience in website developing except for one copied from a lesson
# but if you don't take a step, you won't be able to run the marathon, just saying😅😅
# to be contonued...
plt.show()