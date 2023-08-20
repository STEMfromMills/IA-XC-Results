import pandas as pd

#create Pandas dataframe from Elo-MMR output
runner_data = pd.read_csv("4A.csv",header=0)

#print(runner_data)

'''
#print(runner_data['handle'][0])
handle = ''

handle = str(runner_data['handle'][3000])
print(handle)

handle_without_leading_class = handle.lstrip(handle[0:3])
#print(handle_without_leading_class)

#handle_without_year = handle_without_leading_class[:-5]
#print(handle_without_year)

school_plus = handle_without_leading_class.rsplit(' ',3)[0]
#print(school_plus)

team_ish = handle.split(' ',1)[1].rsplit(' ',3)[0]
#print(team_ish)

team = ''
with open('schools.txt') as school_file:
    for line in school_file:
        if line.rstrip('\n') in team_ish:
            if len(line.rstrip('\n')) > len(team):
                team = line.rstrip('\n')

print(team)
'''   

'''
team = ''
line_length = 0

with open('schools.txt') as school_file:
    for line in school_file:
        i = 0
        line_length = len(line.rstrip('\n'))
        for character in line.rstrip('\n'):
            if character == handle.lstrip(handle[0:3])[i]:
                team = team + character
                i += 1
                if len(team) == line_length:
                    print(team)
                    break
            else:
                team = ''
                break

print(team)        
'''

'''
trimmed_handle =''

trimmed_handle = handle.lstrip(handle[0:3])

#print(trimmed_handle)

team_name = ''

for character in trimmed_handle:
    if character == ' ':
        break
    else:
        team_name = team_name + character

#print(team_name)
'''


'''
def identify_team(runner):


'''

'''
team_rank_list = [[]]
runner_index = 0

for runner in runner_data['handle']:
    if "1A" in runner:
        handle = ''
        handle = str(runner)
        runner_index += 1
        #print(handle)
        handle_without_leading_class = handle.lstrip(handle[0:3])
        school_plus = handle_without_leading_class.rsplit(' ',3)[0]
        team_ish = handle.split(' ',1)[1].rsplit(' ',3)[0]
        team = ''
        with open('schools.txt') as school_file:
            for line in school_file:
                if line.rstrip('\n') in team_ish:
                    if len(line.rstrip('\n')) > len(team):
                        team = line.rstrip('\n')
        #print(team)
        for list in team_rank_list:
            temp_list = []
            list_index = team_rank_list.index(list)
            if team in list:
                temp_list = list
                num_runner = temp_list[1]
                team_points = temp_list[2]
                team_rank_list[list_index].clear()
                if num_runner >= 7:
                    team_rank_list[list_index] = [team,num_runner+1,team_points]
                else:
                    team_rank_list[list_index] = [team,num_runner+1,team_points + runner_data['rank'][runner_index]]
            else:
                team_rank_list.append([team,1,runner_data['rank'][runner_index]])

print(team_rank_list)
'''



'''
team_list = []
runner_list = []
team_total = []


with open('schools.txt') as schools_file:
    for line in schools_file:
        team_list.append(line.rstrip('\n'))
        runner_list.append(0)
        team_total.append(0)
#print(team_list)

runner_index = 0
common_index = 0
for runner in runner_data['handle']:
    common_index = 0
    handle = ''
    handle = str(runner)
    #print(runner_data['rank'][runner_index])
    handle_without_leading_class = handle.lstrip(handle[0:3])
    school_plus = handle_without_leading_class.rsplit(' ',3)[0]
    team_ish = handle.split(' ',1)[1].rsplit(' ',3)[0]
    team = ''
    with open('schools.txt') as school_file:
        for line in school_file:
            if line.rstrip('\n') in team_ish:
                if len(line.rstrip('\n')) > len(team):
                    team = line.rstrip('\n')
    if team not in team_list:
        team = 'ERROR'
    common_index = team_list.index(team)
    if runner_list[common_index] >= 7:
        runner_list[common_index] = runner_list[common_index] + 1
    else:
        runner_list[common_index] = runner_list[common_index] + 1
        team_total[common_index] = team_total[common_index] + runner_data['rank'][runner_index]
    runner_index += 1

combined_list = []
for i in range(len(team_list)):
    combined_list.append([team_list[i],runner_list[i],team_total[i]])

#print(combined_list)

whole_teams_list = []

for team_info in combined_list:
    if team_info[1] >= 7:
        whole_teams_list.append(team_info)

#print(whole_teams_list)

sorted_team_list = []

for team_info in whole_teams_list:
    #print(team_info)
    index = 0
    team_score = team_info[2]
    #print(team_score)
    #print(len(sorted_team_list))
    if len(sorted_team_list) == 0:
        sorted_team_list.append(team_info)
    else:
        while index < len(sorted_team_list) and team_score >= sorted_team_list[index][2]:
            index += 1
        sorted_team_list.insert(index,team_info)

print(sorted_team_list)
'''

#need to create a new data structure of just the top seven of each team for better point totals
#loop through the dataframe and create a new data frame just (new) rank and handle for only seven per team
#maybe look at making a team list and corresponding team number list... counts up to 5 then stops adding that handle

teams_with_at_least_5_runners = []

team_list = []
runner_list = []

with open('schools.txt') as schools_file:
    for line in schools_file:
        team_list.append(line.rstrip('\n'))
        runner_list.append(0)
#print(team_list)

runner_index = 0
common_index = 0
for runner in runner_data['handle']:
    common_index = 0
    handle = ''
    handle = str(runner)
    #print(runner_data['rank'][runner_index])
    handle_without_leading_class = handle.lstrip(handle[0:3])
    school_plus = handle_without_leading_class.rsplit(' ',3)[0]
    team_ish = handle.split(' ',1)[1].rsplit(' ',3)[0]
    team = ''
    with open('schools.txt') as school_file:
        for line in school_file:
            if line.rstrip('\n') in team_ish:
                if len(line.rstrip('\n')) > len(team):
                    team = line.rstrip('\n')
    if team not in team_list:
        team = 'ERROR'
    common_index = team_list.index(team)
    runner_list[common_index] = runner_list[common_index] + 1

combined_list = []
for i in range(len(team_list)):
    combined_list.append([team_list[i],runner_list[i]])

for team in combined_list:
    if team[1] >= 5:
        teams_with_at_least_5_runners.append(team[0])

#print(teams_with_at_least_5_runners)
#print(len(teams_with_at_least_5_runners))

#create new ranking of just the top seven, six, or five of each member within the "teams_with_at_least_5_members"
#three separate lists to track - teams with at least 5 runners, how many have been accounted for (7), and total points (5)
point_scoring_runners_account = []
not_rank_but_score = 1
team_points = []

for i in teams_with_at_least_5_runners:
    point_scoring_runners_account.append(0)
    team_points.append(0)
 
teams_with_at_least_5_runners.append("All Others")
point_scoring_runners_account.append(0)
team_points.append(0)

#print(teams_with_at_least_5_runners)
'''
if "NORTHWOOD-KENSETT" in teams_with_at_least_5_runners:
    print("NK is here!")
else:
    print("not here")
'''
#print(point_scoring_runners_account)
#print(team_points)

point_scoring_only_handles = []

for runner in runner_data['handle']:
    common_index = 0
    handle = ''
    handle = str(runner)
    #print(runner_data['rank'][runner_index])
    handle_without_leading_class = handle.lstrip(handle[0:3])
    school_plus = handle_without_leading_class.rsplit(' ',3)[0]
    team_ish = handle.split(' ',1)[1].rsplit(' ',3)[0]
    team = ''
    for entry in teams_with_at_least_5_runners:
        if entry in team_ish:
            if len(entry) > len(team):
                team = entry
    if team not in teams_with_at_least_5_runners:
        team = "All Others"
    common_index = teams_with_at_least_5_runners.index(team)
    if point_scoring_runners_account[common_index] < 5:
        point_scoring_runners_account[common_index] = point_scoring_runners_account[common_index] + 1
        team_points[common_index] = team_points[common_index] + not_rank_but_score
        not_rank_but_score += 1
        point_scoring_only_handles.append(runner)
    elif point_scoring_runners_account[common_index] < 7:
        point_scoring_runners_account[common_index] = point_scoring_runners_account[common_index] + 1
        not_rank_but_score += 1
        point_scoring_only_handles.append(runner)
    else:
        pass
#print(len(point_scoring_only_handles))

combined_list = []
for i in range(len(teams_with_at_least_5_runners)):
    combined_list.append([teams_with_at_least_5_runners[i],point_scoring_runners_account[i],team_points[i]])
#print(combined_list)

sorted_team_list = []

for team_info in combined_list:
    #print(team_info)
    index = 0
    team_score = team_info[2]
    #print(team_score)
    #print(len(sorted_team_list))
    if len(sorted_team_list) == 0:
        sorted_team_list.append(team_info)
    else:
        while index < len(sorted_team_list) and team_score >= sorted_team_list[index][2]:
            index += 1
        sorted_team_list.insert(index,team_info)

#print(sorted_team_list)

ranking = 1
for team in sorted_team_list:
    print(str(ranking) + ". " + team[0])
    ranking += 1