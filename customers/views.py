from django.shortcuts import render, redirect, get_object_or_404
from .models import Customers
from .forms import CustomerForm

def customer_list(request):
    customers = Customers.objects.all()
    return render(request, 'customers/customer_list.html', {'customers': customers})

def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'customers/customer_form.html', {'form':form})

def customer_update(request, id):
    customer = get_object_or_404(Customers, id=id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customers/customer_form.html', {'form': form})

def customer_delete(request, id):
    customer = get_object_or_404(Customers, id=id)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'customers/customer_confirm_delete.html', {'customer': customer})

def customer_detail(request, id):
    customer = get_object_or_404(Customers, id=id)
    return render(request, 'customers/customer_detail.html', {'customer': customer})

