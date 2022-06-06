from rest_framework import serializers
from .models import Birmingham_Vibe, entertainment, restaurants

class Birmingham_Vibe_Serializer(serializers.ModelSerializer):
    class Meta:
        model = restaurants
        fields = ['tastes of birmingham', 'ranked birmingham restaurants', 'open hours']

    class Meta:
        model = entertainment
        fields = ['theme parks', 'museums', 'sports events', 'concerts', 'parks', 'open hours'] 
           