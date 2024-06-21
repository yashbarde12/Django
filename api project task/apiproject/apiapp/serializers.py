
from rest_framework import serializers

 
class Userserializer(serializers.Serializer):
    name = serializers.CharField(label = "Enter name:")
    age = serializers.IntegerField(label = "Enter age:")
    salary = serializers.IntegerField(label = "Enter salary:")