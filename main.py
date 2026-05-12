
from pyscript import document, display
import numpy as np

# Suppress matplotlib font logs
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

import matplotlib.pyplot as plt

# Preload to avoid font cache message
plt.figure()
plt.plot([0, 1], [0, 1])
plt.close()

# Store data globally
months = []
absences = []


def displaying(e):
    month = document.getElementById('mOfTheWeek').value
    absence = int(document.getElementById('absences').value)

    # Save data
    months.append(month)
    absences.append(absence)

    # Convert to NumPy array
    converted_absences = np.array(absences)

    # Clear previous plot
    plt.clf()

    # Create graph
    plt.plot(months, converted_absences, marker='o')
    plt.title("Weekly Attendance (Absences)")
    plt.xlabel("month")
    plt.ylabel("Number of Absences")
    plt.grid()

    # Display plot
    plt.show()