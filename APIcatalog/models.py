from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image_url = models.CharField(max_length=2083, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image_url = models.CharField(max_length=2083, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.name}'

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=255, unique=True, blank=True, null=True)
    on_offer = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, null= True, related_name="products")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null= True, related_name="products")
    tags = models.ManyToManyField(Tag, blank=True, related_name="products")
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    min_quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image_url = models.CharField(max_length=2083, blank=True, null=True)

    def __str__(self):
        return f'{self.code} - {self.name}'

