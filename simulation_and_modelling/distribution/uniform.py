import seaborn as sns
import matplotlib.pyplot as plt  


from scipy.stats import uniform
import numpy as np 

n = 10000
start = 10
width = 20
data_uniform = uniform.rvs(size=n, loc=start, scale=width)


ax = sns.histplot(data_uniform,
                  bins=100,
                  kde=True,
                  color='skyblue',
                  stat="density",  
                  linewidth=15,  
                  alpha=1) 


ax.set(xlabel='Uniform Distribution', ylabel='Density')


plt.show()
