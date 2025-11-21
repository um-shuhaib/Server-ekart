from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

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

    def total_rating(self):
        # review_list = Review.objects.filter(product_instance=self)
        review_list= self.review_set.filter(product_instance=self)      # modelname_set
        rating_list = [review.rating for review in review_list]
        return sum(rating_list)/len(rating_list)
    
class Cart(models.Model):
    product_instance = models.ForeignKey(Product,on_delete=models.CASCADE)
    user_instance = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=20,default="in-cart")

    def __str__(self):
        return self.product_instance.product_name
    
class Order(models.Model):
    cart_instance=models.ForeignKey(Cart,on_delete=models.CASCADE)
    user_instance=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.TextField()
    status=models.CharField(max_length=20,default="order-placed")

    def __str__(self):
        return f"{self.user_instance.username}+{self.cart_instance.product_instance.product_name}"
    

class Review(models.Model):
    user_instance=models.ForeignKey(User,on_delete=models.CASCADE)
    product_instance=models.ForeignKey(Product,on_delete=models.CASCADE)
    comment=models.TextField()
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)]) # import validator le minvaluevalidator and maxvaluevalidator

    class Meta:
        unique_together=("user_instance","product_instance")

    def __str__(self):
        return f"{self.product_instance.product_name}+{self.comment}"