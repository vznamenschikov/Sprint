from .models import *
from rest_framework import serializers

from datetime import datetime


class PerevalSerializer(serializers.Serializer):
    # Serializer to convert JSON to dbPereval

    pereval_id = serializers.IntegerField()
    beautyTitle = serializers.CharField()
    title = serializers.CharField()
    other_titles = serializers.CharField()
    connect = serializers.CharField(allow_blank=True)
    add_time = serializers.DateTimeField(allow_null=True, required=False)
    user = serializers.JSONField()
    coords = serializers.JSONField()
    type = serializers.CharField()
    level = serializers.JSONField()
    images = serializers.JSONField()


    def create(self, validated_data):
        lst = ['beautyTitle', 'title', 'other_titles', 'connect', 'pereval_id', 'user', 'coords', 'type', 'level']
        raw_data = {}
        for name in lst:
            raw_data[name] = validated_data.pop(name)

        pereval = dbPereval(date_added=validated_data.pop('add_time', datetime.now()), raw_data=raw_data,
                          images=validated_data.pop('images'))
        pereval.save()
        return pereval

