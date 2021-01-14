from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
from django.contrib.auth.models import User


class Place(models.Model):
    """Table to track places of tasks, such as kitchen, garden..."""
    place_name = models.CharField(default='default place',max_length=300)

    def __str__(self):
        return self.place_name

def get_default_task_place():
    """Get a default place for new task, create one if needed."""
    return Place.objects.get_or_create(place_name="default place")[0]

class Task(models.Model):
    """Table of the different tasks that have to be done, such as 'clean table', 'hover carpet'...."""
    task_name = models.CharField(max_length=200)
    task_points = models.IntegerField(default=5,validators=[MinValueValidator(0), MaxValueValidator(100)])
    task_description = models.CharField(default='default task_description', max_length=600)
    task_place = models.ForeignKey(Place, default=get_default_task_place, on_delete=models.CASCADE)
    task_frequency = models.IntegerField(default=7,validators=[MinValueValidator(0), MaxValueValidator(365)])

    def __str__(self):
        return self.task_name

def get_default_menagio_task():
    """Get a default task for every new menagio"""
    return Task.objects.get_or_create(task_name="default task")[0]

def get_default_user():
    """Get a default user for every new menagio"""
    return User.objects.get_or_create(first_name="default user")

class Menagio(models.Model):
    """Table of the diferent times a task was done. A menagio describes every time a task has been completed."""
    menagio_task = models.ForeignKey(Task, default=get_default_menagio_task, on_delete=models.CASCADE)
    menagio_time = models.DateTimeField
    menagio_team_mate = models.ForeignKey(User, default=get_default_user, on_delete=models.CASCADE)
