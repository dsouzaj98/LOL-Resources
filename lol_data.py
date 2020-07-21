import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats


#reads dataset in from kaggle into pandas
lol_data=pd.read_csv("data/high_diamond_ranked_10min.csv")


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
print(len(red_data.columns))
for idx in range(len(red_data.columns)):
    tstat, pval=stats.ttest_ind(red_data.iloc[:,idx], blue_data.iloc[:,idx])
    tstats.append(tstat)
    pvals.append(pval)

new_names=[]
for col in red_data.columns:
    new_names.append(col[3:])
   
df=pd.DataFrame(list(zip(tstats, pvals)), index=new_names, columns=["T-stat", "P-value"])





#win likelihood calculations
P_bluew=(lol_data["blueWins"].mean())
P_redw=1-P_bluew


#cleans data and creates heatmap
#cleaned_lol_data=lol_data.drop(["gameId", "blueGoldDiff", "redGoldDiff", "blueExperienceDiff", "redExperienceDiff", "redFirstBlood", "blueFirstBlood"], axis=1)
# corr=cleaned_lol_data.corr()
# plt.figure(figsize=(12,7))
# ax=plt.subplot()
# sns.heatmap(corr, ax=ax)
# plt.show()