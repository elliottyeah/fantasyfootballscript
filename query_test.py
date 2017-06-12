import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'fantasyfootball.settings'
from players.models import Player
Player.objects.filter(player_position="Defender" , buy_value__lte=7.0).order_by(('expected').desc())[:5]