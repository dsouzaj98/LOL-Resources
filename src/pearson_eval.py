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
ax.set_title("Correlation Heat Map")
plt.show()


#Scatterplot of means by category
def scatterplot(rdata, bdata):
    for idx in range(len(rdata.columns)):
        data1=rdata.iloc[:,idx]
        data2=bdata.iloc[:,idx]
        pear, pval=stats.pearsonr(data1, data2)
        # print(rdata.columns[idx][3:], pear, pval)
        # print(f"{rdata.columns[idx]} vs.  {bdata.columns[idx]}")
        # print('Red Data: mean=%.3f stdv=%.3f    Blue Data: mean=%.3f stdv=%.3f ' % (np.mean(data1), np.std(data1),np.mean(data2), np.std(data2)), pear)
        fig2, ax2=plt.subplots(1,1, figsize=(14,7))
        ax2.scatter(data1, data2, color="orange")
        ax2.set_title(f"{red_data.columns[idx]} vs. {blue_data.columns[idx]}")
        ax2.set_xlabel(red_data.columns[idx])
        ax2.set_ylabel(blue_data.columns[idx])
        ax2.text(0.6,0.8, f"Pearson value: {pear.round(3)}   P-value: {pval.round(3)}", style="oblique", fontsize=12, color="Black", transform=plt.gca().transAxes)
        plt.show()

scatterplot(red_data, blue_data)
    
