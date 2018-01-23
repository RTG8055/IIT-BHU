import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_excel('Final.xlsx')

print data["SNAVER"]

sns.distplot(data["SNAVER"])
plt.show()