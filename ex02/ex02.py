import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'name': ['christopher', 'marion', 'maria', 'mia', 'clement', 'randy', 'remi'],
    'age': [70, 30, 22, 19, 45, 33, 20],
    'gender': ['M', 'F', 'F', 'F', 'M', 'M', 'M'],
    'state': ['california', 'dc', 'california', 'dc', 'california', 'new york', 'porto'],
    'num_children': [4, 2, 1, 0, 3, 1, 0],
    'num_pets': [5, 1, 0, 2, 2, 2, 3]
})

ax = df.plot(x='age', y='num_children', kind='scatter', figsize=(8, 6))
ax.set_title('Age vs Number of Children')
ax.set_xlabel('age')
ax.set_ylabel('num_children')
plt.tight_layout()
plt.show()

print("No clear relationship observed between age and number of children.")