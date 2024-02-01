from rest_framework import serializers
from .models import Comment

class CommentSerialaizerIn(serializers.Serializer):
    age = serializers.IntegerField()
    name = serializers.CharField(max_length=24)
    englishLevel = serializers.CharField(max_length=12)

class CommentSerialaizerIn(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['age', 'name', 'englishLevel']

class CommentSerialaizerOut(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'age', 'name', 'englishLevel', 'status']


class ItemSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=240)
    discount = serializers.BooleanField()
    price = serializers.FloatField()




    # age = serializers.IntegerField()
    # name = serializers.CharField(max_length=240)
    # englishLevel = serializers.CharField(max_length=4)

