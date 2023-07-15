import pandas as pd

#create Pandas dataframe from Elo-MMR output
runner_data = pd.read_csv("all_players.csv",header=0)

#print(runner_data)
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


for runner in runner_data['handle']:
    handle = ''
    handle = str(runner)
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
    print(team)


