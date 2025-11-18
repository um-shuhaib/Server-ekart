from django.db import models

# Create your models here.
class Category(models.Model):
    category=models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.category
    
class Product(models.Model):
    Category_instance=models.ForeignKey(Category,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=200)
    description=models.TextField()
    price=models.PositiveIntegerField()
    image=models.ImageField(upload_to="product_image")

    def __str__(self):
        return self.product_name