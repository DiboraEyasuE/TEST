import matplotlib.pyplot as plt
import numpy as np


# Simple line plot of temperature versus the days in a week
days = [1, 2, 3, 4, 5, 6, 7]
temperature = [72, 75, 68, 70, 74, 77, 71]

plt.plot(days, temperature)
plt.show()