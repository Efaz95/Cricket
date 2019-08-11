from random import randint
from time import sleep

# creating a toss class
class Toss():
    def toss(self):
        choice = ["heads", "tails"]
        return choice[randint(0, 1)]

class Team():
    def __init__(self, team_name, player_names=list()):
        self.team_name = team_name
        self.player_names = player_names

    def view_players(self):
        """ This is a quite useless method that basically prints the names of a chosen team's players line by line """
        for name in self.player_names:
            print(name) 

class Player():
    """ The "run" method should take a player and a run that that player has made and associate the run with that player only """
    def __init__(self, user_players, opponent_players):
        self.user_players = user_players
        self.opponent_players = opponent_players
 
    # this is mainly where I am currently stuck. Why does "+= run" not increment the run of the player!? 
    # Should I create player_run_dict in the init method?    
    def run(self, player, run):
        player_run_dict = {player: 0}
        player_run_dict[player] += run
        
      
user_team = Team(input("Enter your team name: "), player_names=input("Enter your players, seperated by commas: ").split(", "))
opposing_team = Team("Opposing Team") # opposing team is so "creatively" called Opposing Team :) 

# setting up opposing team players
# this will reflect the number of players the user has on their team
count = 1
for player in range(len(user_team.player_names)):
    opposing_team.player_names.append("Player " + str(count))
    count += 1
 
# Initiating a Toss simulation
toss = Toss()

# Assigning Heads or Tails to both teams
user_team.toss_choice = input("Heads or Tails: ").lower()
opposing_team.toss_choice = "heads" if user_team.toss_choice == "tails" else "tails"

# Let's check who won and who'll play what
if user_team.toss_choice == toss.toss():
    print("You have won the toss")
    user_choice = input("Bat or Ball: ")
    user_team.playing = 'Batting' if user_choice == "Bat" else "Balling"
    opposing_team.playing = "Balling" if user_team.playing == "Batting" else "Batting"
else:
    print("You have lost")
    bat_or_ball = ["Bat", "Ball"]
    opponent_choice = bat_or_ball[randint(0, 1)]
    opposing_team.playing = "Batting" if opponent_choice == "Bat" else "Balling"
    user_team.playing = "Balling" if opposing_team.playing == "Batting" else "Batting"

print(f"You are {user_team.playing}")
print(f"Opposing team is {opposing_team.playing}")

# beginning game
wickets = len(user_team.player_names) - 1
balls = 6

player = Player(user_team.player_names, opposing_team.player_names)

while balls != 0: 
    if user_team.playing == "Batting":
        user_batsmen = user_team.player_names
        playing_batsmen = user_batsmen[:1]
        current_batsman = playing_batsmen[0]
        run = randint(0,7)
        if run != 7:
            print(f"Wow! Your player scored {run} runs")
            if run in [1, 3, 5]:
                pass
                # player change
            else:
                pass
                # player remains same
        elif run == 7:
            print("Out!!")
            # and player changes to a player that was previously NOT in the "playing batsmen" list

    print("Ball done")
    sleep(1)
    print("Next ball comin' up")
    balls -= 1