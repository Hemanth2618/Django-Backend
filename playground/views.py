
# Description of various functions of Django ORM

from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product
from django.db import transaction
from django.db import connection

# In transaction module, there is a function called atomic which can be used as decorator or context manager

# Q class is for executing multiple queries using OR operator
# AND operator can be easily done by chaining the filter methods or giving multiple arguments in a filter method
# F class is for referencing fields in a query. Eg: inventory = F('unit_price'). We can also reference a field in a related table.
# Eg: filter(inventory=F('collection__id')) # It is like JOIN
# Create your views here.

# @transaction.atomic() # The whole view function can be atomic
def say_hello(request):
    # Reading the Objects from Database
    '''query_set = Product.objects.filter(unit_price__range=(20, 30))
    query_set = Product.objects.filter(unit_price__gt=20)
    query_set = Product.objects.values('id', 'title')
    query_set = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    query_set = Product.objects.filter(inventory=F('unit_price'))'''

    # Creating the objects in database (Inserting data into database)
    '''Two Ways: 1st Way
    collection = Collection() -> Creating an object of a model (table in database)
    collection.title = "Video Games"
    collection.featured_product = Product(pk=1) -> I am using a Product object to assign value to this field
    collection.save() -> To insert this object into database, we should call this method
    2nd Way:
    collection = Collection.objects.create(title = "Video Games", featured_product_id = 1)
    The create method returns an object after the row is inserted into database'''

    # Updating the objects in database (Updating the records in table)
    '''Two Ways: 1st Way
    collection = Collection.objects.get(pk=1) -> Creating an object of a model (table in database)
    collection.featured_product = None
    collection.save()
    2nd Way:
    Collection.objects.filter(pk = 11).update(featured_product=None)'''

    # Deleting the objects in Database (Deleting the record in database)
    '''collection = Collection(pk = 11)
    collection.delete()
    Deleting multiple objects
    Collection.objects.filter(id__gt = 5).delete()'''

    # Transaction Processing in Django (Multiple changes happening in atomic way. If one change fails all others should be rolled back)
    # Wrapping both the below code blocks in transaction block
    '''with transaction.atomic():
        order = Order()
        order.customer_id = 1
        order.save()
    
        item = OrderItem()
        item.order = order
        item.product_id = 1
        item.quantity = 1
        item.save()'''

    # Executing raw SQL queries
    '''query_set = Product.objects.raw('SELECT * FROM store_product')
    return render(request, 'hello.html', {'name': 'Hemanth', 'products': list(query_set)})
    Another way of executing raw SQL queries:
    with connection.cursor() as cursor:
        cursor.callproc('get_customers', [1, 2, 3]) # Calling SQL procedures'''

