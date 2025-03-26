## Django Imports ##
from django.shortcuts import get_object_or_404, get_list_or_404
## Rest Framework Imports ##
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

## Brand ##
# Models imports #
from .models import Brand
from .serializers import BrandSerializer

# HTTP Methods #
# GET All (Public)#
@api_view(['GET'])
def GetBrands(request):
    brands = Brand.objects.all()
    brands_serializer = BrandSerializer(brands, many=True)
    return Response({'brands': brands_serializer.data}, status=status.HTTP_200_OK)

# GET One by ID (Public)#
@api_view(['GET'])
def GetBrand(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    brand_serializer = BrandSerializer(brand)
    return Response({'brand': brand_serializer.data}, status=status.HTTP_200_OK)

# POST (Private)#
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def CreateBrand(request):
    brand_serializer = BrandSerializer(data=request.data)
    if brand_serializer.is_valid():
        brand_serializer.save()
        return Response({'brand': brand_serializer.data}, status=status.HTTP_201_CREATED)

    return Response(brand_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# DELETE by ID (Private)#
@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def DeleteBrand(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    brand.delete()
    return Response({'message':'Deleted Successfully'},status=status.HTTP_204_NO_CONTENT)

# PUT by ID (Private)#
@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def UpdateBrand(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    brand_serializer = BrandSerializer(brand, data=request.data)
    if brand_serializer.is_valid():
        brand_serializer.save()
        return Response({'brand': brand_serializer.data}, status=status.HTTP_200_OK)

    return Response(brand_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

## Category ##

from .models import Category
from .serializers import CategorySerializer

@api_view(['GET'])
def GetCategories(request):
    categories = Category.objects.all()
    categories_serializer = CategorySerializer(categories, many=True)
    return Response({'categories': categories_serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def GetCategory(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category_serializer = CategorySerializer(category)
    return Response({'category': category_serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def CreateCategory(request):
    category_serializer = CategorySerializer(data=request.data)
    if category_serializer.is_valid():
        category_serializer.save()
        return Response({'category': category_serializer.data}, status=status.HTTP_201_CREATED)

    return Response(category_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def DeleteCategory(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return Response({'message':'Deleted Successfully'},status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def UpdateCategory(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category_serializer = CategorySerializer(category, data=request.data)
    if category_serializer.is_valid():
        category_serializer.save()
        return Response({'category': category_serializer.data}, status=status.HTTP_200_OK)

    return Response(category_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

## Tag ##
from .models import Tag
from .serializers import TagSerializer

@api_view(['GET'])
def GetTags(request):
    tags = Tag.objects.all()
    tags_serializer = TagSerializer(tags, many=True)
    return Response({'tags': tags_serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def GetTag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    tag_serializer = TagSerializer(tag)
    return Response({'tag': tag_serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def CreateTag(request):
    tag_serializer = TagSerializer(data=request.data)
    if tag_serializer.is_valid():
        tag_serializer.save()
        return Response({'tag': tag_serializer.data}, status=status.HTTP_201_CREATED)

    return Response(tag_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def DeleteTag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    tag.delete()
    return Response({'message':'Deleted Successfully'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def UpdateTag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    tag_serializer = TagSerializer(tag, data=request.data)
    if tag_serializer.is_valid():
        tag_serializer.save()
        return Response({'tag': tag_serializer.data}, status=status.HTTP_200_OK)

    return Response(tag_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

## Product ##
# Models imports #
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
def GetProducts(request):
    products = Product.objects.all()
    products_serializer = ProductSerializer(products, many=True)
    return Response({'products': products_serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def GetProduct(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product_serializer = ProductSerializer(product)
    return Response({'product': product_serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def GetProductsByCategoryID(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    product_serializer = ProductSerializer(products, many=True)
    return Response({'products': product_serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def CreateProduct(request):

    product_serializer = ProductSerializer(data=request.data)
    if product_serializer.is_valid():
        product_serializer.save()
        return Response({'product': product_serializer.data}, status=status.HTTP_201_CREATED)

    return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def DeleteProduct(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return Response({'message':'Deleted Successfully'},status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def UpdateProduct(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product_serializer = ProductSerializer(product, data=request.data)
    if product_serializer.is_valid():
        product_serializer.save()
        return Response({'product': product_serializer.data}, status=status.HTTP_200_OK)

    return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

