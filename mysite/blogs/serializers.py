from rest_framework import serializers
from blogs.models import Category

# create serializers

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Category
        fields="__all__"
