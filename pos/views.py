from time import process_time_ns
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
import json
from django.db.models import Q 

from django_pos.views import detect

from .models import Product, Customer, Order, OrderItem

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required(login_url='login')
def billing(request):
    if request.method == 'GET':
        return render(request, 'billing.html')
    else:
        cid = request.POST.get('customerID', None)
        customer = Customer.objects.get(pk=cid)
        products = list(Product.objects.all())
        # context = { 'cust' : customer.identity,
        #             'name' : customer.name,
        #             'balance' : customer.balance,
        #             'products': products, }
        return render(request, 'billing_details.html', {'customer': customer, 'products': products})



@login_required
def search_username(request):
    if request.method == 'POST':
        searchedq = request.POST.get('customername')
        searcheduser = Customer.objects.filter(
            Q(name__contains = searchedq) |
            Q(last_name__contains = searchedq)
            )
        return render(request, 'billing.html',{'searcheduser':searcheduser})
   
    else:
        return render(request, 'billing.html')
       








@login_required(login_url='login')
def order(request):
    if request.method == 'POST':
        
        data = json.loads(request.POST.get('data', None))
        if data is None:
            raise AttributeError
        print(data)
        customer = Customer.objects.get(pk=data['customer_id'])
        fc = detect(request)
        if fc != 0:
            if str(fc) == str(customer.userId):
                global order
                order = Order.objects.create(customer=customer,
                                            total_price=data['total_price'],
                                            success=False)
                for product_id in data['product_ids']:
                    OrderItem(product=Product.objects.get(pk=product_id), order=order).save()
                if data['total_price'] <= customer.balance:
                    customer.balance -= int(data['total_price'])
                    customer.save()
                    order.success = True
                order.save()
            else:
                # order = "transaction failed, Due to Incorrect faceID provided"
                order.success = False
        else:
            print('not found')
        
        return render(request, 'order.html', {'success' : order.success})
        # return render(request, 'order.html')

def User_login(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else '/')

        else:
            messages.error(request, 'Username OR password is incorrect')
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('login')