import json
import csv
import time
#NOTES#
#Put all csv stats in a json payload Home Team and Away Team Then we will pass both of those to a function to calculate between the two teams.
#print(home_team_stats["Defense First Downs"])




def gather_teams():
    #Gather Name of teams playing, by default the home team will get an additional point for being at home. 
    home_team_name = input('What is the name of the home team: ')
    home_team_report(home_team_name)
    
def home_team_report(home_team_name):
    print('Generating stats for the home team: '+home_team_name)
    with open(home_team_name+'.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            d_first_downs = row['def_first_downs']
            d_pass_yards = row['def_pass_yds']
            d_rush_yards = row['def_rush_yds']
            d_total_yards = row['def_total_yds']
            d_turnovers = row['def_turnovers']
            o_first_downs = row['off_first_down']
            o_pass_yards = row['off_pass_yds']
            o_rush_yards = row['off_rush_yds']
            o_total_yards = row['off_total_yds']
            o_turnovers = row['off_turnovers']
            d_points_allowed = row['points_allowed']
            o_points_scored = row['points_scored']
            total_wins = row['wins']
            total_losses = row['losses']
        
            x = '{"name":"'+home_team_name+'", "Defense First Downs":'+d_first_downs+', "Defense Pass Yards":'+d_pass_yards+', "Defense Rush Yards":'+d_rush_yards+', "Defense Total Yards":'+d_total_yards+', "Defense Turnovers Gained":'+d_turnovers+', "Offense First Downs":'+o_first_downs+', "Offense Pass Yards":'+o_pass_yards+', "Offense Rush Yards":'+o_rush_yards+', "Offense Total Yards":'+o_total_yards+', "Offense Turnovers":'+o_turnovers+', "Defense Points Allowed":'+d_points_allowed+', "Offense Points Scored":'+o_points_scored+', "Total Wins":'+total_wins+', "Total Losses":'+total_losses+', "Home Advantage":1}'
            home_team_stats = json.loads(x)
            #print(home_team_stats)
            away_team_report(home_team_stats)


def away_team_report(home_team_stats):
    away_team_name = input('What is the name of the away team: ')
    print('Generating stats for the away team: '+away_team_name)
    with open(away_team_name+'.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            d_first_downs = row['def_first_downs']
            d_pass_yards = row['def_pass_yds']
            d_rush_yards = row['def_rush_yds']
            d_total_yards = row['def_total_yds']
            d_turnovers = row['def_turnovers']
            o_first_downs = row['off_first_down']
            o_pass_yards = row['off_pass_yds']
            o_rush_yards = row['off_rush_yds']
            o_total_yards = row['off_total_yds']
            o_turnovers = row['off_turnovers']
            d_points_allowed = row['points_allowed']
            o_points_scored = row['points_scored']
            total_wins = row['wins']
            total_losses = row['losses']

            x = '{"name":"'+away_team_name+'", "Defense First Downs":'+d_first_downs+', "Defense Pass Yards":'+d_pass_yards+', "Defense Rush Yards":'+d_rush_yards+', "Defense Total Yards":'+d_total_yards+', "Defense Turnovers Gained":'+d_turnovers+', "Offense First Downs":'+o_first_downs+', "Offense Pass Yards":'+o_pass_yards+', "Offense Rush Yards":'+o_rush_yards+', "Offense Total Yards":'+o_total_yards+', "Offense Turnovers":'+o_turnovers+', "Defense Points Allowed":'+d_points_allowed+', "Offense Points Scored":'+o_points_scored+', "Total Wins":'+total_wins+', "Total Losses":'+total_losses+', "Home Advantage":0}'
            away_team_stats = json.loads(x)
            #print(away_team_stats)
            calculate_winning_team(home_team_stats, away_team_stats)


def calculate_winning_team(home_team_stats, away_team_stats):
        home_team_points = 1
        away_team_points = 0

        #Checking who has less first downs against.
        if home_team_stats["Defense First Downs"] < away_team_stats["Defense First Downs"]:
            home_team_points = home_team_points + 1
        else:
            away_team_points = away_team_points + 1

        #Checking who has less pass yards against.
        if home_team_stats["Defense Pass Yards"] < away_team_stats["Defense Pass Yards"]:
            home_team_points = home_team_points + 1 
        else:
            away_team_points = away_team_points + 1
        
        #Checking who has less run yards against.
        if home_team_stats["Defense Rush Yards"] < away_team_stats["Defense Rush Yards"]:
            home_team_points = home_team_points + 1 
        else:
            away_team_points = away_team_points + 1

        #Checking total yards against.
        if home_team_stats["Defense Total Yards"] < away_team_stats["Defense Total Yards"]:
            home_team_points = home_team_points + 2
        else:
            away_team_points = away_team_points + 2

        #Checking total defensive turnovers. 
        if home_team_stats["Defense Turnovers Gained"] > away_team_stats["Defense Turnovers Gained"]:
            home_team_points = home_team_points + 1
        else:
            away_team_points = away_team_points + 1
        
        #Checking Offense First Downs. 
        if home_team_stats["Offense First Downs"] > away_team_stats["Offense First Downs"]:
            home_team_points = home_team_points + 1
        else:
            away_team_points = away_team_points + 1
        
        #Checking Offense Passing Yards.
        if home_team_stats["Offense Pass Yards"] > away_team_stats["Offense Pass Yards"]:
            home_team_points = home_team_points + 1
        else:
            away_team_points = away_team_points + 1

        #Checking Offense Rushing Yards. 
        if home_team_stats["Offense Rush Yards"] > away_team_stats["Offense Rush Yards"]:
            home_team_points = home_team_points + 1
        else:
            away_team_points = away_team_points + 1

        #Checking Offense Total Yards. 
        if home_team_stats["Offense Total Yards"] > away_team_stats["Offense Total Yards"]:
            home_team_points = home_team_points + 2
        else:
            away_team_points = away_team_points + 2

        #Checking who has more offensive turnovers.
        if home_team_stats["Offense Turnovers"] < away_team_stats["Offense Turnovers"]:
            home_team_points = home_team_points + 1
        else:
            away_team_points = away_team_points + 1

        #Checking what defense has allowed less points.
        if home_team_stats["Defense Points Allowed"] < away_team_stats["Defense Points Allowed"]:
            home_team_points = home_team_points + 1
        else:
            away_team_points = away_team_points + 1

        #Checking Total Offense Points. 
        if home_team_stats["Offense Points Scored"] > away_team_stats["Offense Points Scored"]:
            home_team_points = home_team_points + 2
        else:
            away_team_points = away_team_points + 2

        #Checking Total Wins. 
        if home_team_stats["Total Wins"] > away_team_stats["Total Wins"]:
            home_team_points = home_team_points + 1
        else:
            away_team_points = away_team_points + 1

        #Checking Total Losses
        if home_team_stats["Total Losses"] < away_team_stats["Total Losses"]:
            home_team_points = home_team_points + 1
        else:
            away_team_points = away_team_points + 1


        #Calculating Winner
        if home_team_points > away_team_points:
            print("After Calculation, we belive that the home team "+home_team_stats["name"]+" will win the contest.")
        else:
            print("After calculation, we belive that the away team "+away_team_stats["name"]+" will win the contest.")

        #Explination
        time.sleep(1)
        print('The stats are as follows: '+home_team_stats["name"]+' has the points of: '+str(home_team_points))
        print(home_team_points)
        print('The stats are as follows: '+away_team_stats["name"]+' has the points of: '+str(away_team_points))
        print(away_team_points)
        
        





gather_teams()

