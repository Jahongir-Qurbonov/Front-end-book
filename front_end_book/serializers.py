from rest_framework import serializers
from .models import Element, ElementExample, ElementAttributes, AttributeExample

class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        exclude = ['id','information','collection']


class CollectionElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        exclude = ['id']


class ExampleElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElementExample
        fields = ['example_code']

    
class AttributesElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElementAttributes
        exclude = ['id', 'element']

class ExampleAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeExample
        fields = ['example','information']