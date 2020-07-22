# Pa=prob of win
# pb=prob of column
# pa|b= prob of win given column
# pb|a=prob of col given win

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt 
import pandas as pd 
plt.style.use("ggplot")

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


#creates beta distribution plot
def plot_beta(alpha, beta, ax, title=None, label=None, xticks=[0.0,0.5,1.0]):
    dist=stats.beta(alpha, beta)
    x=np.linspace(0.0,1.0,301)
    y=dist.pdf(x)

    lines=ax.plot(x,y, label=label)
    ax.fill_between(x,y,alpha=0.2, color=lines[0].get_c())
    if title:
        ax.set_title(title)
    ax.get_yaxis().set_ticks([])
    ax.get_xaxis().set_ticks(xticks)
    #ax.set_ylim(0.0,np.max(y)*1.2)

alpha_values=red_data["redFirstBlood"].mean()
beta_values=blue_data["blueFirstBlood"].mean()
#alpha_beta_pairs=((i,j) for i in alpha_values for j in beta_values)


#create list of means for each column
rmeans=[]
bmeans=[]


# for col in red_data.columns:
#     for elem in red_data[col]:
#         if elem>=red_data[col].mean():
#             rmeans.append(elem)

# for idx in range(len(red_data.columns)):
#     rmean=red_data.iloc[:,idx].mean()
#     bmean=blue_data.iloc[:,idx].mean()
#     if 
           