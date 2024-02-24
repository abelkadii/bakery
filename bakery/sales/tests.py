from django.test import TestCase
from .models import *
# Create your tests here.

# products = [{'name': 'apple', 'price': 1.0950693399838145, 'stock': 68, 'category': 'dairy'}, {'name': 'banana', 'price': 5.603508959036905, 'stock': 84, 'category': 'dairy'}, {'name': 'orange', 'price': 3.609463864701137, 'stock': 74, 'category': 'beverage'}, {'name': 'grape', 'price': 8.905012832436144, 'stock': 81, 'category': 'vegetable'}, {'name': 'strawberry', 'price': 6.681981051479765, 'stock': 76, 'category': 'beverage'}, {'name': 'blueberry', 'price': 8.63624396952329, 'stock': 85, 'category': 'dairy'}, {'name': 'kiwi', 'price': 9.812147293240793, 'stock': 81, 'category': 'fruit'}, {'name': 'watermelon', 'price': 5.9407084377780475, 'stock': 22, 'category': 'dairy'}, {'name': 'pineapple', 'price': 6.150284419204631, 'stock': 67, 'category': 'dairy'}, {'name': 'mango', 'price': 5.000177427272283, 'stock': 37, 'category': 'fruit'}]

# for order in orders:
    # Order.objects.create(product=order['product'], quantity=order['quantity'], total=order['total'], created=order['created_at'])