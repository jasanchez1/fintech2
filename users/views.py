from .models import Transaction
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import TransactionForm, UserRegistrationForm
from django.template import loader
from django.http import HttpResponse
from datetime import datetime

def home(request):
    return render(request, 'users/home.html')

def historial(request):
    return render(request, 'users/historial.html')

def transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            return HttpResponse('/thanks/')
    return render(request, 'users/transaction.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)

def historial(request):
    latest_transaction_list = Transaction.objects.order_by('-pub_date')[:5]
    context = {'latest_transaction_list': latest_transaction_list}
    return render(request, 'users/historial.html', context)

def transaction_form(request):
    if request.GET['qty'] != '0':
        Transaction(len(Transaction.objects.all()), request.GET['crypto'], request.GET['transtype'], int(request.GET['qty']), str(datetime.now()), int(request.GET['userId'])).save()
    return historial(request)
