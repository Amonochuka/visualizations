import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 3, figsize=(12, 8))
fig.subplots_adjust(hspace=0.5, wspace=0.5)

for i, ax in enumerate(axes.flat, 1):
    ax.text(0.5, 0.5, f'(2,3,{i})', ha='center', va='center', fontsize=14, transform=ax.transAxes)
    ax.set_title(f'Title {i}')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

plt.show()