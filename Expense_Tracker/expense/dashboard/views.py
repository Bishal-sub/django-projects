from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import expense_model_Form
from .models import expense_model
from django.db.models import Sum


# Create your views here.
def home(request):
    return render(request, "home.html")


@login_required
def create_expense(request):
    if request.method == "POST":
        form = expense_model_Form(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect("expense")
    else:
        form = expense_model_Form()

    return render(request, "add_expense.html", {"form": form})


@login_required
def update_expesne(request, id):
    data = expense_model.objects.get(id=id, user = request.user)
    if request.method == "POST":
        form = expense_model_Form(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect("expense")
    else:

        form = expense_model_Form(instance=data)
    return render(request, "update_expense.html", {"form": form})


@login_required
def expense(request):
    form = expense_model.objects.filter(user = request.user)
    total = expense_model.objects.filter(user=request.user).aggregate(Sum("amount"))
    name = request.user.username
    return render(request, "expense.html", {"form": form,"total":total,"name":name})

@login_required
def delete_expense(request, id):

    data = expense_model.objects.filter(id=id, user = request.user)
    data.delete()

    return redirect("expense")
