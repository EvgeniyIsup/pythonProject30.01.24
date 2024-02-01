from django.db import models

# Create your models here.
class Comment(models.Model):
    age = models.IntegerField()
    name = models.TextField()
    englishLevel = models.CharField(max_length=4)
    status = models.CharField(max_length=24)
    def __init__(self, age, name, englishLevel):
        allowedLevel = ["B3", "B4"]
        self.age = age
        self.name = name
        self.englishlevel = englishLevel
        self.status = "Принят" if self.englishlevel in allowedLevel and self.age > 25 else "НЕ принят"

class Item():
    def __init__(self, name, discount, price):
        self.name = name
        self.discount = discount
        self.price = price * 0.9 if discount else price
