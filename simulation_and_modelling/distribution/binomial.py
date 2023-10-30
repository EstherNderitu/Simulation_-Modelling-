import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import binom

# Generate random numbers from a binomial distribution
data_binom = binom.rvs(n=10, p=0.8, size=10000)

# Create a histogram without a density plot (kde=False)
ax = sns.histplot(data_binom,
                  kde=False,
                  color='skyblue',
                  bins=100,
                  linewidth=15,
                  alpha=1)

# Set labels
ax.set(xlabel='Binomial Distribution', ylabel='Frequency')

# Show the plot
plt.show()
