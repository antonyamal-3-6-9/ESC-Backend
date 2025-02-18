from django.db import models

# Create your models here.

class RootCategory(models.Model):
    name = models.CharField(max_length=255)
    
class MainCategory(models.Model):
    name = models.CharField(max_length=255)

class Product(models.Model):
    root = models.ForeignKey(RootCategory, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    main = models.ForeignKey(MainCategory, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    
    features = models.JSONField(null=True, blank=True)
    material = models.CharField(max_length=255, null=True, blank=True)
    condition = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="product_images/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.product.name}"
