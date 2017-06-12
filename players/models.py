from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=40)#
    #first_name = models.CharField(max_length=40)
    #last_name = models.CharField(max_length=40, default="elli")
    #points_last_three = models.CharField(max_length=40, default="elli")
    #expected_next_three = models.CharField(max_length=40, default="elli")
    team_name = models.CharField(max_length=40)
    player_position = models.CharField(max_length=40)
    buy_value = models.DecimalField(max_digits=4, decimal_places=2)
    next_three = models.CharField(max_length=40)
    last_three = models.CharField(max_length=40)
    expected = models.DecimalField(max_digits=20,decimal_places=10,default=0.0) #changed from char
    expected_three = models.IntegerField(default=0)
    idn = models.CharField(max_length=40)
    news = models.CharField(max_length=120)
    chance_of_playing = models.CharField(max_length=40, blank="true")

    def __str__(self):
        return self.name

#fields = ['first_name','last_name','team_name','player_position','buy_value','next_three','last_three','points_last_three','expected_next_three','idn','news']