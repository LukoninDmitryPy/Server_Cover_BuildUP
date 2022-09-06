from rest_framework import serializers

from buildup.models import Unit


class FileSerializer(serializers.ModelSerializer):
    reach = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        fields = ('unit', 'reach')
        model = Unit
