from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


def customer_photo_directory(instance, filename):
    return 'customers/{0}_{1}'.format(instance.userId, instance.name)

  
  
 
    


class Customer(models.Model):

    type_choices=(
        ("yes","yes "),
        ("no","no"),
    )
    userId = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)
    occupation = models.CharField(max_length=150, null=True)
    bank = models.CharField(max_length=50, null=True)
    card_number = models.CharField(max_length=50, null=True)
    balance = models.DecimalField(max_digits=6, decimal_places=2)
    blacklisted = models.CharField(max_length=50,choices =type_choices,default='no')
    #display_photo = models.ImageField(upload_to=customer_photo_directory, null=True)

    def __str__(self):
        return '{0} ({1})'.format(self.userId, self.name)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    success = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Order {0}'.format(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
