from django.shortcuts import render,  redirect
from .forms import CustomerForm
from django.contrib import messages



# Create your views here.
def register_customers(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        global user_id
        if form.is_valid():
            form.save()
            user_id = request.POST['userId']
            # user = form.save(commit=False)
            # user.save()
            # messages.success(request, 'User account was created!')

            # login(request, user)
            # return redirect('register_face/')
            # print("success")
            return redirect('face_url')
        else:
            messages.success(request, 'An error has occurred during registration')
    else:
        form = CustomerForm()

    context = {"form":form}
    return render(request, 'customer_onboarding/customer_registration.html', context)

def register_face(request):
    context = {"userId":user_id}
    return render(request, 'customer_onboarding/test.html', context)

def thank_page(request):
    return render(request, 'customer_onboarding/success_page.html')