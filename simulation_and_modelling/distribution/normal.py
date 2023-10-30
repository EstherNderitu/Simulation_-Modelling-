import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm


data_normal = norm.rvs(size=10000, loc=0, scale=1)


ax = sns.histplot(data_normal,
                  bins=100,
                  kde=True,
                  color='skyblue',
                  linewidth=15,
                  alpha=1)


ax.set(xlabel='Normal Distribution', ylabel='Frequency')


plt.show()
