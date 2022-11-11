from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = []

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        exclude = ['question']

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(read_only=True, many=True)
    class Meta:
        model = Question
        exclude = []
        depth = 1

class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        exclude = []
        depth = 1