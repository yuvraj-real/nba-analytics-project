-- Top 10 Teams by Total Rebounds
SELECT Tm, SUM(TRB) as Total_Rebounds
From player_logs
Group By Tm
ORDER BY Total_Rebounds DESC
Limit 10;


-- Top 10 Scorers (Minimum 5 games played)
SELECT Player, Tm, COUNT(Date) as Games, ROUND(AVG(PTS), 1) as PPG
FROM player_logs
GROUP BY Player
HAVING Games >= 5
ORDER BY PPG DESC
LIMIT 10;


-- Best Performers by Average Game Score (Minimum 5 games played)
SELECT Player, Tm, COUNT(Date) as Games, ROUND(AVG("GmSc"), 1) as Average_Game_Score,  ROUND(AVG(PTS), 1) as PPG
FROM player_logs
GROUP BY Player
HAVING Games >= 5
ORDER BY Average_Game_Score DESC
LIMIT 10;


-- Best Individual Performances by Points in Losses
SELECT Player, Tm, Date, PTS, TRB, AST, GmSc 
FROM player_logs
WHERE Result = 'L'
GROUP BY Date
ORDER BY PTS DESC
LIMIT 10;