from django.db import models



class Product(models.Model):
    productCategories = [('Food', 'Food'), ('Drink', 'Drink'), ("fruit", "fruit"), ("vegetable", "vegetable"), ("meat", "meat"), ("dairy", "dairy"), ("beverage", "beverage")]
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=productCategories)
    price = models.FloatField()
    stock = models.IntegerField(name="stock")
    # image_url = models.CharField(max_length=2083)
    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    total = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.quantity} of {self.product.name} at {self.total} DH"
    
class Restock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.quantity} of {self.product.name} at {self.created}"