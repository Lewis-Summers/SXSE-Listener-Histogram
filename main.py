import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from random import randint, choices, random, choice
import pandas as pd

# Number of data points
age_groups = [[18,24], [25,34], [35, 44], [45, 54], [55, 64]]
listeners = [36, 44, 13, 5, 2]
genders = [[0.4, 0.6], [0.4, 0.6], [0.1, 0.9], [0.05, 0.95], [0.05, 0.95]]
ageDS = []
genderDS = []
for listener, ages, gender in zip(listeners, age_groups, genders):
    for i in range(listener*100):
        ageDS.append(randint(ages[0], ages[1]))
        genderDS.append(choices(["Female", "Male"], weights=gender, k=1)[0])
        # genderDS.append(choice(gender))

print(len(ageDS))
# Example data
people_data = {
    'Age': ageDS,
    'Gender': genderDS
}
people_df = pd.DataFrame(people_data)

# Create a 2D density plot
# sns.kdeplot(x=ageDS, y=genderDS, fill=True, cmap='viridis', cbar=True)
# plt.title('Age and Gender Density')
# plt.xlabel('Age')
# plt.ylabel('Density')
# plt.show()
# Create a 2D histogram
plt.figure(figsize=(10, 6))
sns.histplot(data=people_df, x='Age', y='Gender', cbar=True, cmap='viridis')
plt.title('Age and Gender Density Of J Cole Listeners')
plt.xlabel('Age')
plt.ylabel('Gender')
plt.show()