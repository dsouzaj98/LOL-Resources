import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 
lol_data=pd.read_csv("data/high_diamond_ranked_10min.csv")


fig, ax=plt.subplots(1,1)
KDA_df=pd.DataFrame()
KDA_df["game number"]=np.arange(1,len(lol_data+1))
KDA_df["blueKDA"]=(lol_data["blueKills"]+lol_data["blueAssists"])/lol_data["blueDeaths"]
KDA_df["redKDA"]=(lol_data["redKills"]+lol_data["redAssists"])/lol_data["redDeaths"]


ax.plot(KDA_df["game number"], KDA_df["blueKDA"], '-b')
ax.plot(KDA_df["game number"],KDA_df["redKDA"], '-r')
plt.axis('tight')
plt.title('KDA Blue vs. Red')
plt.xlabel("Game Number")
plt.ylabel("KDA")
plt.show()
