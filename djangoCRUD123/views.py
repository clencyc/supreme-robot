from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Student


def index(request):
    data = Student.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)


def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")


def edit(request):
    return render(request, "edit.html")


def login_page(request):
    return render(request, "login.html")


def signup_page(request):
    return render(request, "signup.html")


def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        course = request.POST.get('course')
        gender = request.POST.get('gender')


        query = Student(name=name, email=email, age=age, course=course, gender=gender)
        query.save()
        return redirect("/")

        return render(request, 'index.html')


def deleteData(request, id):
    d = Student.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, "index.html")


def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')

        course = request.POST.get('city')
        gender = request.POST.get('gender')


        update_info = Student.objects.get(id=id)
        update_info.name = name
        update_info.email = email
        update_info.age = age

        update_info.course = course
        update_info.gender = gender


        update_info.save()
        return redirect("/")

    d = Student.objects.get(id=id)
    context = {"d": d}
    return render(request, "edit.html", context)

