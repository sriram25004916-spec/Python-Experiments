run_scored=int(input("Enter the Run scorted by Player :"))
print(run_scored)
ball_faced=int(input("Enter the Ball faced by Player :"))
print(ball_faced)
fours=int(input("Enter the total Fours hits  by Player :"))
print(fours)
sixes=int(input("Enter the Total Sixes hits by Player :"))
print(sixes)
wickets_taken=int(input("Enter the wicket taken by Player :"))
print(wickets_taken)
run_conc=int(input("Enter the Run conceeded by Player :"))
print(run_conc)
overs_bowled=int(input("Enter the over bowled by Player :"))
print(overs_bowled)
catch_taken=int(input("Enter the catch taken by Player :"))
print(catch_taken)

print("Calculating the batting strike rate of player:")
sr=(run_scored/ball_faced)*100
print(sr)
print("Calculating the Balling Economy of player:")
eco=(run_conc/overs_bowled)
print(eco)

batter=1
if run_scored>=50 and sr>=120:
    print("Execellent Batter:")
elif run_scored>=30 and sr>=100:
    print("Good Batter")
elif run_scored>=20:
    print("Average Batter")
else :
    print("Poor Batter")

bowler=1
if wickets_taken>=3 and eco<=6:
    print("Execellent Bowler:")
elif wickets_taken>=2 and eco<=8:
    print("Good Bowler")
elif wickets_taken>=1:
    print("Average Bowler")
else :
    print("Poor Bowler")

if catch_taken>=2:
    print("Outstanding Fielder")
elif catch_taken == 1:
    print("Active Player")
else :
    print("Need improvement")


print("Overall All-Rounder Decission:")
if batter==1 and bowler==1:
    print("Star All-rounder")
elif batter==2 and bowler==2:
    print("Strong All-Rounder")
elif batter==3 and bowler==3:
    print("Supporting All-Rounder")






