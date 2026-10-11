import matplotlib.pyplot as plt

# Data with different scales - left_data is integers, right_data is decimals
left_data = [5, 7, 11, 13, 17]
right_data = [0.1, 0.2, 0.4, 0.8, -1.6]
x_axis = [0.0, 1.0, 2.0, 3.0, 4.0]

fig, ax1 = plt.subplots(figsize=(8, 6))

# Left y-axis (primary) - black
color = 'black'
ax1.set_xlabel('x_axis')
ax1.set_ylabel('left_data', color=color)
ax1.plot(x_axis, left_data, color=color)
ax1.tick_params(axis='y', labelcolor=color)

# Right y-axis (secondary) - red, using twinx for different scale
ax2 = ax1.twinx()
color = 'red'
ax2.set_ylabel('right_data', color=color)
ax2.plot(x_axis, right_data, color=color)
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Matplotlib Twinx Dual-Axis Plot')
fig.tight_layout()
plt.show()