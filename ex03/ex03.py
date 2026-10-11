import matplotlib.pyplot as plt

# Define data points with integer coordinates
x = [1, 2, 3, 4, 5, 6, 7, 8]
y1 = [1, 2, 3, 4, 5, 6, 7, 8]      # Linear: y = x
y2 = [1, 4, 9, 16, 25, 36, 49, 64]  # Quadratic: y = x^2

plt.figure(figsize=(8, 6))
# Red dashdot line with width 3
plt.plot(x, y1, 'r-.', linewidth=3, label='Line')
# Blue circles with size 12
plt.plot(x, y2, 'bo', markersize=12, label='Points')

plt.title('Matplotlib Custom Plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
# Limit axes to [1, 8] as required
plt.xlim(1, 8)
plt.ylim(1, 8)
plt.legend()
plt.grid(True)
plt.show()