import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
username = os.getenv('FRCUSER')
api_key = os.getenv('KEY')



great_northern = 'NDGF'
granite_city = 'MNMI2'
tournament_levels = ['None','Practice','Qualification', 'Playoffs']

event_code = granite_city
team_number = ''
week_number = ''
tournament_level = tournament_levels[2]
match_number = ''

frc_url = 'https://frc-api.firstinspires.org/v3.0/2025/'
event_list = f'events?eventCode={event_code}&teamNumber={team_number}&districtCode=&excludeDistrict=&weekNumber={week_number}&tournamentType='
event_schedule = f'schedule/{event_code}?tournamentLevel={tournament_level}&teamNumber={team_number}start=&end='
detailed_results = f'scores/{event_code}/{tournament_level}?matchNumber={match_number}&start=&end='
match_results = f'matches/{event_code}?tournamentLevel=qual&teamNumber={team_number}&matchNumber={match_number}&start=&end='
team_list = f'teams?teamNumber=&eventCode={event_code}&districtCode=&state=&page='

url = frc_url + team_list
#print(url)
r = requests.get(url, auth = (username,api_key))
if r.status_code == 200:
    teamdetail = r.json()
else:
    print(f'Error in request {r.status_code}: {r.reason} - {r.text}')

teamdict = {}

for team in teamdetail['teams']:
    teamdict[team['teamNumber']] = team['nameShort']

#print(username)
#print(api_key)
url = frc_url + event_schedule
#print(url)
r = requests.get(url, auth = (username,api_key))
if r.status_code == 200:
    schedule = r.json()
else:
    print(f'Error in request {r.status_code}: {r.reason} - {r.text}')
jsonexport = {}
matches = []
for match in schedule['Schedule']:
    bluestation = []
    redstation = []
    alliance = {}
    qual = {}
    teamarr = {}

    for team in match['teams']:
      alliance['number'] =  team['teamNumber']
      alliance['name']= teamdict[team['teamNumber']]

      if 'Blue' in team['station']:         
          bluestation.append(alliance.copy())
      else:
          redstation.append(alliance.copy())

    teamarr['red'] = redstation
    teamarr['blue'] = bluestation
    qual['matchNumber'] = match['matchNumber']
    qual['matchTime'] = match['startTime']
    qual['teams'] = teamarr


    matches.append(qual)


jsonexport['matches']= matches
#print(schedule['Schedule'][0]['matchNumber'])
#matches.append[{'teamname': schedule['Schedule'][0]['matchNumber']}]
print(json.dumps(jsonexport, indent=4))

