import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#reads dataset in from kaggle into pandas
lol_data=pd.read_csv("data/high_diamond_ranked_10min.csv")

#WardsPlaced
#WardsDestroyed
#FirstBlood
#Kills
#Deaths
#Assists
#EliteMonsters
#Dragons
#Heralds


#For each of the 20 categories that I have selected, I want to create a hypothesis for 
#what I expect the result of the testing to be

#my end goal is to create a ranking of which resources are most valuable



#win likelihood calculations
P_bluew=(lol_data["blueWins"].mean())
P_redw=1-P_bluew

#wardsplaced
P_bluewards=(lol_data["blueWardsPlaced"].mean())
P_redwards=(lol_data["redWardsPlaced"].mean())

# WardsDestroyed
P_bluewards_des=(lol_data["blueWardsDestroyed"].mean())
P_redwards_des=(lol_data["redWardsDestroyed"].mean())

#FirstBlood
P_b_firstblood=(lol_data["blueFirstBlood"].mean())
P_r_firstblood=(lol_data["redFirstBlood"].mean())

#Kills
P_blueKills=(lol_data["blueKills"].mean())
P_redKills=(lol_data["redKills"].mean())

#Deaths
P_blueDeaths=(lol_data["blueDeaths"].mean())
P_redDeaths=(lol_data["redDeaths"].mean())

#assists
P_blue_assists=(lol_data["blueFirstBlood"].mean())
P_red_assists=(lol_data["redFirstBlood"].mean())

#EliteMonsters
P_blueEM=(lol_data["blueEliteMonsters"].mean())
P_redEM=(lol_data["redEliteMonsters"].mean())

#Dragons
P_blueDragons=(lol_data["blueDragons"].mean())
P_redDragons=(lol_data["redDragons"].mean())

#Heralds
P_blueHeralds=(lol_data["blueHeralds"].mean())
P_redHeralds=(lol_data["redHeralds"].mean())

#TowersDestroyed
P_bluetowers=(lol_data["blueTowersDestroyed"].mean())
P_redtowers=(lol_data["redTowersDestroyed"].mean())

#TotalGold
P_blue_gold=(lol_data["blueTotalGold"].mean())
P_red_gold=(lol_data["redTotalGold"].mean())

#AvgLevel
P_bluelevel=(lol_data["blueAvgLevel"].mean())
P_redlevel=(lol_data["redAvgLevel"].mean())

#TotalExperience
P_blue_exp=(lol_data["blueTotalExperience"].mean())
P_red_exp=(lol_data["redTotalExperience"].mean())

#TotalMinionsKilled
P_blue_minions=(lol_data["blueHeralds"].mean())
P_red_minions=(lol_data["redHeralds"].mean())

#TotalJungleMinionsKilled
P_blue_jungle=(lol_data["blueTotalJungleMinionsKilled"].mean())
P_red_jungle=(lol_data["redTotalJungleMinionsKilled"].mean())

#GoldDiff
P_bluegold_diff=(lol_data["blueHeralds"].mean())
P_redgold_diff=(lol_data["redHeralds"].mean())
#ExperienceDiff
P_blue_exp_diff=(lol_data["blueExperienceDiff"].mean())
P_red_exp_diff=(lol_data["redExperienceDiff"].mean())
#CSPerMin
P_blue_CS=(lol_data["blueCSPerMin"].mean())
P_red_CS=(lol_data["redCSPerMin"].mean())
#GoldPerMin
P_blue_gold=(lol_data["blueGoldPerMin"].mean())
P_red_gold=(lol_data["redGoldPerMin"].mean())

cleaned_lol_data=lol_data.drop(["gameId", "blueGoldDiff", "redGoldDiff", "blueExperienceDiff", "redExperienceDiff", "redFirstBlood", "blueFirstBlood"], axis=1)
corr=cleaned_lol_data.corr()
plt.figure(figsize=(15,10))
ax=plt.subplot()
sns.heatmap(corr, ax=ax)
plt.show()