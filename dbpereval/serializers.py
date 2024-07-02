from drf_writable_nested import WritableNestedModelSerializer, UniqueFieldsMixin
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

    def to_representation(self, instance):
        # Возвращает JSON raw_data + images
        raw_data = instance.raw_data
        raw_data['images'] = instance.images
        return raw_data

    def create(self, validated_data):
        # Создание объекта
        lst = ['beautyTitle', 'title', 'other_titles', 'connect', 'pereval_id', 'user', 'coords', 'type', 'level']
        raw_data = {}
        for name in lst:
            raw_data[name] = validated_data.pop(name)

        pereval = dbPereval(date_added=validated_data.pop('add_time', datetime.now()),
                            raw_data=raw_data, images=validated_data.pop('images'))
        pereval.save()
        return pereval

    def update(self, instance, validated_data):
        # Редактирование объекта
        lst = ['beautyTitle', 'title', 'other_titles', 'connect', 'pereval_id', 'coords', 'type', 'level']
        raw_data = {}
        for name in lst:
            raw_data[name] = validated_data.pop(name)

        raw_data['user'] = instance.raw_data.pop('user', '{}')

        pereval = dbPereval(id=instance.id, date_added=validated_data.pop('add_time', instance.date_added),
                            raw_data=raw_data, images=validated_data.pop('images'))
        pereval.save()
        return instance

