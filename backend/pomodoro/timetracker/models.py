from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Schema(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    duration = models.IntegerField()
    standard_break = models.IntegerField()
    long_break = models.IntegerField()
    long_break_delay = models.IntegerField()
    auto_start_pomodoros = models.BooleanField(default=False)
    auto_start_breaks = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    default = models.BooleanField(default=False)

class Pomodoro(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.IntegerField(validators = [MinValueValidator(0)])
    done = models.BooleanField(default=False)