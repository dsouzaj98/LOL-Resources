# League of Legends Win Likelihood
 
In my capstone, I will be using a League of Legends database from kaggle.com describing top players' game statistics for over 10k games.  This dataset can be found at https://www.kaggle.com/bobbyscience/league-of-legends-diamond-ranked-games-10-min.  Using this data, I will be performing a variety of statistical tests to determine which factors in game have the highest effect on win percentage.

Some of the factors I intend to examine include the team color(red vs blue) as the gameplay can vary depending on side, and advantages through resources gained in the first 10 minutes of the game.  It is expected that increased resources(gold, minions, objectives) would reesults in a higher chance of winning the game but my analysis would like to determine which have the greatest impact on the game.

The factors I intend to examine for each team are 
1. Assists 
2. Average Level
3. CS Per Min
4. Deaths
5. Dragons
6. Elite Monsters
7. Experience Differential
8. First Blood
9. Gold Differential
10. Gold Per Min
11. Heralds
12. Kills
13. Total Experience
14. Total Gold
15. Total Jungle Minions
16. Total Minions Killed
17. Towers Destroyed
18. Wards Destroyed
19. Wards Placed


All of the values in the dataset are numerical allowing me to insert my desired columns into the ideal format(panda dataframe).  

My MVP would be to answer the question of "What resource advantage is most likely to help achieve a win?".  My MVP+ would be to establish confidence intervals for all of the categories and relate them to a calculated mean of winning the game to get a definitive number of what extent each resource affects win likelihood?


