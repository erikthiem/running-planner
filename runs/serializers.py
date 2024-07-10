from rest_framework import serializers

from runs.models import Run

class RunSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Run
        fields = ['distance_miles', 'start_time']
