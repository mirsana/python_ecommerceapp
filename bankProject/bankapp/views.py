from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

# Create your views here.

from .form import DataForm
from .models import Data, District, Branch


def index(request):
    return render(request, 'index.html')

def data(request):
    form = DataForm(request.POST or None, request.FILES)
    if form.is_valid():
        # form = DataForm(request.POST or None, request.FILES)
        name = form.cleaned_data['name']
        dob = form.cleaned_data['dob']
        age = form.cleaned_data['age']
        gender = form.cleaned_data['gender']
        phno = form.cleaned_data['phno']
        mail = form.cleaned_data['mail']
        address = form.cleaned_data['address']
        dist = form.cleaned_data['dist']
        branch = form.cleaned_data['branch']
        acType = form.cleaned_data['acType']
        service = form.cleaned_data['service']

        d = Data(name=name, dob=dob, age=age, gender=gender, phno=phno, mail=mail, address=address, acType=acType,
                 dist=dist, branch=branch, service=service)
        d.save();
        messages.info(request, "Application accepted !")
        return redirect('form')
    form = DataForm()
    return render(request, 'form.html', {'form': form})

# def add_data(request):
#     form = DataForm()
#     if request.method == 'POST':
#         name = request.POST.get('name', )
#         dob = request.POST.get('dob', )
#         age = request.POST.get('age', )
#         gender = request.POST.get('gender', )
#         phno = request.POST.get('phno', )
#         mail = request.POST.get('mail', )
#         address = request.POST.get('address', )
#         dist = request.POST.get('dist', )
#         branch = request.POST.get('branch', )
#         acType = request.POST.get('acType', )
#         crCard = True if request.POST.get('crCard', ) == 'on' else False
#         dbCard = True if request.POST.get('dbCard', ) == 'on' else False
#         cqBook = True if request.POST.get('cqBook', ) == 'on' else False
#         d = Data(name=name, dob=dob, age=age, gender=gender, phno=phno, mail=mail, address=address, acType=acType,
#                  dist=dist, branch=branch, creditCard=crCard, debitCard=dbCard, chequebook=cqBook)
#         d.save();
#         return redirect('dataform')
#     return render(request, 'dataform.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('form')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('login')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username not available")
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email not available")
                return redirect('/register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save();
                return redirect('/login')

        else:
            messages.info(request, "Password not matching")
            return redirect('/register')

        return redirect('/')
    return render(request, 'register.html')


# class DataCreateView(CreateView):
#     model = Data
#     form_class = DataForm
#     success_url = reverse_lazy('add')
#
#
# class DataListView(ListView):
#     model = Data
#     context_object_name = 'data'


def load_branch(request):
    dist_id = request.GET.get('dist_id')
    branch = Branch.objects.filter(dist_id=dist_id).all()
    return render(request, 'hr/dropdown_list.html', {'branch': branch})



