# from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Team


# Create your views here.

# def about(request):
# return render(request, "about.html")

# def contact(request):
# return render(request, "contact.html")

# def detail(request):
# return render(request, "detail.html")

# def thanks(request):
# return render(request, "thanks.html")


# def operations(request):
#   return render(request, "operations.html")
# def result(request):
#   num1 = int(request.GET['num1'])
#  num2 = int(request.GET['num2'])
# sum = num1 + num2
# dif = num1 - num2
# pro = num1 * num2
# div = num1 / num2
# return render(request, "result.html", {'sum':sum, 'dif':dif,'pro':pro,'div':div })


# static website example

def index(request):
    # obj = Place.objects.all()
    obj1 = Team.objects.all()
    return render(request, "index.html", {'members': obj1})
    # return render(request, "index.html", {'images': obj})

