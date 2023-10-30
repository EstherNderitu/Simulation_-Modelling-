import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import expon


data_expon = expon.rvs(scale=1, loc=0, size=1000)


ax = sns.histplot(data_expon,
                  kde=True,
                  bins=100,
                  color='skyblue',
                  linewidth=15,
                  alpha=1)


ax.set(xlabel='Exponential Distribution', ylabel='Frequency')


plt.show()
