import pandas as pd 
import numpy as np

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
#TowersDestroyed
#TotalGold
#AvgLevel
#TotalExperience
#TotalMinionsKilled
#TotalJungleMinionsKilled
#GoldDiff
#ExperienceDiff
#CSPerMin
#GoldPerMin

#For each of the 20 categories that I have selected, I want to create a hypothesis for 
#what I expect the result of the testing to be

#my end goal is to create a ranking of which resources are most valuable



#win likelihood calculations
P_bluew=(lol_data["blueWins"].mean())
P_redw=1-P_bluew

#wardsplaced
P_bluewards=(lol_data["blueWardsPlaced"].mean())
P_redwards=(lol_data["redWardsPlaced"].mean())
print(P_bluewards,P_redwards)
