import matplotlib.pyplot as pyplot
import numpy as np

x = np.linspace(0,20,100) # Create a list of evenly-spaced number over the range
plt.plot(x, np.sin(x))    # Plot the sine of each x point
plt.show()                # Display the plot