from random import randint
from time import sleep

class Toss():
    def toss(self):
        choice = ["heads", "tails"]
        return choice[randint(0, 1)]

class Team():
    def __init__(self, team_name, preferred_team=False, player_names=list()):
        self.team_name = team_name
        self.player_names = player_names
        self.preferred_team = preferred_team

    def view_players(self):
        for name in self.player_names:
            print(name) 

class Player():
    def __init__(self, user_players, opponent_players):
        self.user_players = user_players
        self.opponent_players = opponent_players

    def run(self, player, run):
        player_run_dict = {player: 0}
        player_run_dict[player] += run
        

       
user_team = Team(input("Enter your team name: "), player_names=input("Enter your players, seperated by commas: ").split(", "), preferred_team=True)
opposing_team = Team("Opposing Team")

# setting up opposing team players
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
        run = 5
        if run != 7:
            print(f"Wow! Your player scored {run} runs")
            if run in [1, 3, 5]:
                player.run(current_batsman, run)
                # player change
            else:
                pass
                # player remains same
        elif run == 7:
            print("Out!!")

    print("Ball done")
    sleep(1)
    print("Next ball comin' up")
    balls -= 1