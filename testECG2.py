import matplotlib.pyplot as plt
import matplotlib.animation as animation
#from sensores.ecg import ECG

# Parameters
x_len = 800         # Number of points to display
y_range = [0, 4]  # Range of possible Y values to display

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = list(range(0, x_len))
ys = [0] * x_len
ax.set_ylim(y_range)

# Initialize communication with TMP102
#ecg = ECG()

# Create a blank line. We will update the line in animate
line, = ax.plot(xs, ys)

# Add labels
plt.title('ECG')
plt.xlabel('Muestras')
plt.ylabel('Voltaje (V)')

# This function is called periodically from FuncAnimation
def animate(i, ys1):

    # Read temperature (Celsius) from TMP102
    #voltajeECG = round(ecg.getVoltage(), 5)

    # Add y to list
    ys1.append(3)

    # Limit y list to set number of items
    ys1 = ys1[-x_len:]

    # Update line with new Y values
    line.set_ydata(ys1)

    return line,

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig,
    animate,
    fargs=(ys,),
    interval=100,
    blit=True)
plt.show()
