from .models import Element, ElementExample, ElementAttributes, AttributeExample
from .serializers import ElementSerializer, CollectionElementSerializer,\
    ExampleElementSerializer, AttributesElementSerializer, ExampleAttributeSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK

# Create your views here.

@api_view(['get'])
def getUrls(r):
    urls = {
        '.../elements':'barcha elementlarni olish',
        '.../elements/<name>/':'element nomi orqali elementni olish',
        '.../collections':'to\'plamga tegishli elementlarni olish',
        '.../collections/<collection>/':'to\'plamga tegishli elementni olish'        
    }
    return Response(urls, status=HTTP_200_OK)


@api_view(['get'])
def getElements(r):
    element = Element.objects.all()
    serializer = ElementSerializer(element, many=True)
    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['get'])
def getSingleElement(r, name):
    element = Element.objects.get(name=name)
    serializer = ElementSerializer(element)
    data = serializer.data

    elementExample = ElementExample.objects.filter(element=element)
    example_serializer = ExampleElementSerializer(elementExample, many=True)
    data['example_code'] = []
    for v in example_serializer.data:
        data['example_code'].append(v['example_code'])
    

    elementAttributes = ElementAttributes.objects.filter(element=element)
    attributes_serializer = AttributesElementSerializer(elementAttributes, many=True)
    attr_data = attributes_serializer.data

    aExample = AttributeExample.objects.filter(element=element)
    for i ,v in enumerate(elementAttributes):
        attributeExample = aExample.filter(attribute=v)
        attrExample_serializer = ExampleAttributeSerializer(attributeExample, many=True)
        attr_data[i]['example']=attrExample_serializer.data

    data['attributes'] = attr_data
    return Response(data=data, status=HTTP_200_OK)

@api_view(['get'])
def getCollections(r):
    element = Element.objects.exclude(collection=None)
    serializer = CollectionElementSerializer(element, many=True)
    return Response(serializer.data, status=HTTP_200_OK)

@api_view(['get'])
def getCollection(r, collection):
    elements = Element.objects.filter(collection=collection).order_by('name')

    datas = []

    for element in elements:
        serializer = ElementSerializer(element)
        data = serializer.data

        elementExample = ElementExample.objects.filter(element=element)
        example_serializer = ExampleElementSerializer(elementExample, many=True)
        data['example_code'] = []
        for v in example_serializer.data:
            data['example_code'].append(v['example_code'])
        
        elementAttributes = ElementAttributes.objects.filter(element=element)
        attributes_serializer = AttributesElementSerializer(elementAttributes, many=True)
        attr_data = attributes_serializer.data

        aExample = AttributeExample.objects.filter(element=element)
        for i ,v in enumerate(elementAttributes):
            attributeExample = aExample.filter(attribute=v)
            attrExample_serializer = ExampleAttributeSerializer(attributeExample, many=True)
            attr_data[i]['example']=attrExample_serializer.data

        data['attributes'] = attr_data
        datas.append(data)
    return Response(data=datas, status=HTTP_200_OK)