import requests
import os
from dotenv import load_dotenv

load_dotenv()
username = os.getenv('FRCUSER')
api_key = os.getenv('KEY')



great_northern = 'NDGF'
granite_city = 'MNMI2'

event_code = ''
team_number = ''
week_number = ''
tournament_level = ''
match_number = ''

tournament_levels = ['None','Practice','Qualification', 'Playoffs']
frc_url = 'https://frc-api.firstinspires.org/v3.0/2025/'
event_list = f'events?eventCode={event_code}&teamNumber={team_number}&districtCode=&excludeDistrict=&weekNumber={week_number}&tournamentType='
event_schedule = f'schedule/{event_code}?tournamentLevel={tournament_level}&teamNumber={team_number}start=&end='
detailed_results = f'scores/{event_code}/{tournament_level}?matchNumber={match_number}&start=&end='
match_results = f'matches/{event_code}?tournamentLevel=qual&teamNumber={team_number}&matchNumber={match_number}&start=&end='



print(username)
print(api_key)
r = requests.get(frc_url + event_list, auth = (username,api_key))
if r.status_code == 200:
    print(r.json())
else:
    print(f'Error in request {r.status_code}: {r.reason} - {r.text}')