import sys
import os
import csv
sys.path.append(os.path.abspath(os.path.curdir))
os.environ['DJANGO_SETTINGS_MODULE'] = 'fantasyfootball.settings'
from players.models import Player

player_file = 'playerout.csv'
with open(player_file,'rb') as f:
    reader = csv.reader(f,delimiter=',')
    for row in reader:
        player = Player(name = row[0], team_name = row[1], player_position = row[4], buy_value = row[2], next_three = row[5], last_three =row[6], expected= row[10], idn = row[9], news =row[3], chance_of_playing =row[8] , expected_three=row[11])
        try:
            player.save()
        except:
            # if the're a problem anywhere, you wanna know about it
            print "there was a problem with line"
            raise


