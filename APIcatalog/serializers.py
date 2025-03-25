from rest_framework import serializers
from APIcatalog.models import Brand, Category, Tag, Product

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id','name','image_url']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','image_url']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','name']

class ProductSerializer(serializers.ModelSerializer):

    ## Campos que solo se piden en la creación (no se muestran en la respuesta)
    brand_id = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all(), source='brand', write_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True)
    tags_ids = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), source='tags', many=True, write_only=True)

    ## Campos que solos se muestran en la respuesta (no se piden en la creación)
    brand = BrandSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'code', 'on_offer', 'price', 'brand', 'category', 'tags', 'quantity', 'min_quantity', 'image_url', 'brand_id', 'category_id', 'tags_ids']

    def create(self, validated_data):
        brand = validated_data.pop('brand', None)
        category = validated_data.pop('category', None)
        tags = validated_data.pop('tags', [])

        product = Product.objects.create(
            **validated_data,
            brand=brand,
            category=category
        )
        product.tags.set(tags)
        return product
