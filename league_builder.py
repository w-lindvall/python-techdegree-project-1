import csv

# sample data in 'soccer_players.csv'
filename = 'soccer_players.csv'

# team names (3)
team_names = ('Sharks', 'Dragons', 'Raptors')


# get player information from csv file
def read_csv():
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        player_info = list(reader)
        return player_info


# divide players into two groups based on experience
def make_experience_groups(player_info):
    experienced_players = []
    new_players = []

    for player in player_info:
        if player['Soccer Experience'] == 'YES':
            experienced_players.append(player)
        else:
            new_players.append(player)
    return experienced_players, new_players


# divide players
def fill_teams(experience_group):
    for player in experience_group:
        if experience_group.index(player) % 3 == 0:
            team_1.append(player)
        elif experience_group.index(player) % 3 == 2:
            team_2.append(player)
        elif experience_group.index(player) % 3 == 1:
            team_3.append(player)


# open and write team roster and info to text file
def create_file(team_1, team_2, team_3):
    file = open('teams.txt', 'w')

    teams = [team_1, team_2, team_3]
    for team_name in team_names:
        file.write(team_name + '\n' + '-'*10 + '\n')
        for player in teams[team_names.index(team_name)]:
            file.write(player['Name'])
            if player['Soccer Experience'] == 'YES':
                file.write(' (new), ')
            else:
                file.write(' (experienced), ')
            file.write(player['Guardian Name(s)'] + '\n')
        file.write('\n')


if __name__ == '__main__':
    player_info = read_csv()
    experienced_players, new_players = make_experience_groups(player_info)

    team_1 = []
    team_2 = []
    team_3 = []
    fill_teams(experienced_players)
    fill_teams(new_players)

    create_file(team_1, team_2, team_3)