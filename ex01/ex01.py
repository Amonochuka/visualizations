import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'name': ['christopher', 'marion', 'maria', 'mia', 'clement', 'randy', 'remi'],
    'age': [70, 30, 22, 19, 45, 33, 20],
    'gender': ['M', 'F', 'F', 'F', 'M', 'M', 'M'],
    'state': ['california', 'dc', 'california', 'dc', 'california', 'new york', 'porto'],
    'num_children': [2, 0, 0, 3, 8, 1, 4],
    'num_pets': [5, 1, 0, 5, 2, 2, 3]
})

ax = df.plot(x='name', y=['num_children', 'num_pets'], kind='bar', figsize=(10, 6))
ax.set_title('Number of Children and Pets by Name')
ax.set_xlabel('name')
ax.legend()
plt.tight_layout()
plt.show()