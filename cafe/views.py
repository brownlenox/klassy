from django.shortcuts import render, redirect, get_object_or_404
from . forms import EmployeesForm, OffersForm, LoginForm
from . models import Employees, Offers

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def chefs(request):
    employees = Employees.objects.all()
    return render(request, 'chefs.html', {"employees":employees})

def menu(request):
    return render(request, 'menu.html')

def offers(request):
    offers = Offers.objects.all()
    return render(request, 'offers.html', {'offers':offers})

@login_required
def staff(request):
    employees = Employees.objects.all()
    offers = Offers.objects.all()
    return render(request, 'admin.html',{"employees":employees, "offers":offers})

def employees(request):
    if request.method == 'POST':
        form = EmployeesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EmployeesForm
    return render(request, 'forms/employees.html', {"form":form})

def foods(request):
    return render(request, 'forms/foods.html')

def offerform(request):
    if request.method == 'POST':
        form = OffersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = OffersForm()
    return render(request, 'forms/offers-form.html', {"form":form})

def reservation(request):
    return render(request, 'reservation.html')


# deleteing employee
def employee_delete(request, emp_id):
    employee = get_object_or_404(Employees, pk=emp_id)
    employee.delete()
    return redirect("admin")

#updating employee
def employee_update(request, emp_id):
    employee = get_object_or_404(Employees, pk=emp_id)  # SELECT * FROM employees WHERE id=1
    if request.method == "POST":
        form = EmployeesForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = EmployeesForm(instance=employee)
    return render(request, "forms/employee_update.html", {"form": form})

#deleting offers
def offers_delete(request, emp_id):
    offer = get_object_or_404(Offers, pk=emp_id)
    offer.delete()
    return redirect("admin")

#updating offers
def offers_update(request, emp_id):
    offer = get_object_or_404(Offers, pk=emp_id)  # SELECT * FROM employees WHERE id=1
    if request.method == "POST":
        form = OffersForm(request.POST, request.FILES, instance=offer)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = OffersForm(instance=offer)
    return render(request, "forms/offers_update.html", {"form": form})


def signin(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "forms/signin.html", {"form": form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('staff')
        messages.error(request, "Wrong username or password")
        return render(request, "forms/signin.html", {"form": form})


@login_required
def signout(request):
    logout(request)
    return redirect('signin')

