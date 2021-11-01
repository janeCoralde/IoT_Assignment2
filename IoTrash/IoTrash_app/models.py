from django.db import models

class Room(models.Model):
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = 'Room'
		verbose_name_plural = 'Rooms'
	name = models.CharField (max_length=30, default=None, help_text='Enter name of room in the house, e.g. Kitchen')
	description = models.TextField(max_length=500, blank=True, default=None)

# Create your models here.
class Trash(models.Model):
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = 'Smart Trashcan Name'
		verbose_name_plural = 'Smart Trashcan Names'
		ordering = ['-name']

	name = models.CharField (max_length=30, blank=True, default=None, help_text='Enter name of trash can')
	room = models.ForeignKey(Room, on_delete=models.PROTECT, verbose_name="Specify Room ")
	description = models.TextField(max_length=500, blank=True, default=None)
	times_changed = models.IntegerField(default=int(0))
	sensor_depth = models.IntegerField(blank=True, default=None)
