import sys
import os
sys.path.append(os.path.abspath(os.path.curdir))
os.environ['DJANGO_SETTINGS_MODULE'] = 'fantasyfootball.settings'
from players.models import Player
import django
django.setup()

all_players = Player.objects.all()
for player in all_players:
    player.delete()