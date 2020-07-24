import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
import math
import wordninja


#reads dataset in from kaggle into pandas
lol_data=pd.read_csv("data/high_diamond_ranked_10min.csv")


#separates data based on team color
red_data=lol_data.drop(['gameId','blueWins', 'blueWardsPlaced', 'blueWardsDestroyed',
       'blueFirstBlood', 'blueKills', 'blueDeaths', 'blueAssists',
       'blueEliteMonsters', 'blueDragons', 'blueHeralds',
       'blueTowersDestroyed', 'blueTotalGold', 'blueAvgLevel',
       'blueTotalExperience', 'blueTotalMinionsKilled',
       'blueTotalJungleMinionsKilled', 'blueGoldDiff', 'blueExperienceDiff',
       'blueCSPerMin', 'blueGoldPerMin'], axis=1)
blue_data=lol_data.drop(['gameId','blueWins','redWardsPlaced', 'redWardsDestroyed', 'redFirstBlood', 'redKills',
       'redDeaths', 'redAssists', 'redEliteMonsters', 'redDragons',
       'redHeralds', 'redTowersDestroyed', 'redTotalGold', 'redAvgLevel',
       'redTotalExperience', 'redTotalMinionsKilled',
       'redTotalJungleMinionsKilled', 'redGoldDiff', 'redExperienceDiff',
       'redCSPerMin', 'redGoldPerMin'], axis=1)



#creates Dataframe of pvalues and t statistics
tstats=[]
pvals=[]
for idx in range(len(red_data.columns)):
    tstat, pval=stats.ttest_ind(red_data.iloc[:,idx], blue_data.iloc[:,idx])
    tstats.append(round(tstat,4))
    pvals.append(round(pval,4))
new_names=[]
for col in red_data.columns:
    new_names.append(col[3:])
df=pd.DataFrame(list(zip(tstats, pvals)), index=new_names, columns=["T-stat", "P-value"])
ttest=df.to_markdown()




#graphs normal distributions
for idx in range(len(red_data.columns)):
    fig1, ax1=plt.subplots(1,1, figsize=(12,7))
    rmean=red_data.iloc[:,idx].mean()
    bmean=blue_data.iloc[:,idx].mean()
    red_dist=stats.norm(rmean, red_data.iloc[:,idx].std())
    blue_dist=stats.norm(bmean, blue_data.iloc[:,idx].std())
    x_range=np.linspace(red_dist.ppf(0.01), red_dist.ppf(0.99),101)
    ax1.plot(x_range, red_dist.pdf(x_range), color="red")
    ax1.plot(x_range, blue_dist.pdf(x_range), color="blue")
    ax1.set_title(label=' '.join(wordninja.split(red_data.columns[idx][3:])))
    ax1.set_xlabel(f" {' '.join(wordninja.split(red_data.columns[idx][3:]))}")
    ax1.set_ylabel("Percentile")
    ax1.axvline(red_dist.mean(), color="red", linestyle=':')
    ax1.axvline(blue_dist.mean(), color="blue", linestyle=':')
    ax1.text(0.35,0.2,f" Red Mean: {round(rmean, 3)}   Blue Mean: {round(bmean, 3)} ", transform=plt.gca().transAxes)
    plt.show()

    






