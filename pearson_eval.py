import numpy as np
from scipy import stats
import matplotlib.pyplot as plt 
from lol_data import red_data, blue_data, lol_data
import seaborn as sns


#cleans data and creates heatmap
cleaned_lol_data=lol_data.drop(["gameId", "blueGoldDiff", "redGoldDiff", "blueExperienceDiff", "redExperienceDiff", "redFirstBlood", "blueFirstBlood"], axis=1)
corr=cleaned_lol_data.corr()
plt.figure(figsize=(12,7))
ax=plt.subplot()
sns.heatmap(corr, ax=ax)
plt.show()


#Scatterplot of means by category
for idx in range(len(red_data.columns)):
    data1=red_data.iloc[:,idx]
    data2=blue_data.iloc[:,idx]
    covariance=np.cov(data1, data2)
    pear, pval=stats.pearsonr(data1, data2)
    # print(f"{red_data.columns[idx]} vs.  {blue_data.columns[idx]}")
    # print('Red Data: mean=%.3f stdv=%.3f' % (np.mean(data1), np.std(data1)), pear)
    fig2, ax2=plt.subplots(1,1, figsize=(14,7))
    ax2.scatter(data1, data2, color="orange")
    ax2.set_title(f"{red_data.columns[idx]} vs. {blue_data.columns[idx]}")
    ax2.set_xlabel(red_data.columns[idx])
    ax2.set_ylabel(blue_data.columns[idx])
    ax2.text(0,0, f"Pearson value: {pear}   P-value: {pval}", style="oblique", fontsize=12, color="Black")
    plt.savefig(f"Scatterplot_of_{red_data.columns[idx]}_vs._{blue_data.columns[idx]}.png")
    
