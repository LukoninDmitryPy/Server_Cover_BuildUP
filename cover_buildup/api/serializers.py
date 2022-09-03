from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from buildup.models import Unit, Reach

class ReachSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reach
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    reach = 'serializers.SerializerMethodField()'


    class Meta:
        fields = '__all__'
        model = Unit
