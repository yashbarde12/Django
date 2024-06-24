from rest_framework import serializers



class Userserializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    age = serializers.IntegerField()
    salary = serializers.IntegerField()