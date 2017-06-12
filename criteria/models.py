from django.db import models

# Create your models here.
class Cash(models.Model):
	cash_option = models.DecimalField(max_digits=5, decimal_places=1)
	
	
	def __str__(self):
		return self.cash_option	

class Position(models.Model):
	player_position = models.CharField(max_length=3)
	
	def __str__(self):
			return self.player_position		

#cfields = ['cash_option']
#pfields = ['player_position']