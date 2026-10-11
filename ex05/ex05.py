import matplotlib.pyplot as plt

# Create 2x3 grid of subplots
fig, axes = plt.subplots(2, 3, figsize=(12, 8))
# Add spacing between subplots
fig.subplots_adjust(hspace=0.5, wspace=0.5)

# Loop through all 6 subplots
for i, ax in enumerate(axes.flat, 1):
    # Center text at (0.5, 0.5) using ha='center' for horizontal alignment
    ax.text(0.5, 0.5, f'(2,3,{i})', ha='center', va='center', fontsize=14, transform=ax.transAxes)
    ax.set_title(f'Title {i}')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

plt.show()