import matplotlib.pyplot as plt
import numpy as np

# Create data: 100 points from 0 to 10
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plotting
plt.plot(x, y, label='Sine Wave', color='teal')
plt.title('Simple Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()
plt.grid(True)

# Show the result
plt.show()