from contextlib import _RedirectStream
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


# Create your views here.
def home(request):
    allColleges = College.objects.all()  # select * from college
    context = {
        "colleges": allColleges
    }
    return render(request, 'index.html', context)

# detail page


def detail(request, id):
    college = College.objects.get(id=id)  # select * from college where id=id

    context = {
            "college": college
        }
    return render(request, 'details.html', context)


# add colleges to the database
def add_colleges(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
           if request.method == "POST":
            form = CollegeForm(request.POST or None)

           # check if the form is valid
            if form.is_valid():
             data = form.save(commit=False)
             data.save()
             return redirect("app1:home")
           else:
            form = CollegeForm()
            return render(request, 'addcolleges.html', {"form": form, "controller": "Add Colleges"})

        # if they are not admin
        else:
           return redirect("app1:home")

    # if they are not loggedin
    return redirect("accounts:login")

# edit the college


def edit_colleges(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:

            # get the college linked with id
            college = College.objects.get(id=id)

            # form check
            if request.method == "POST":
                  form = CollegeForm(request.POST or None, instance=college)
                   # check if form is valid
                  if form.is_valid():
                       data = form.save(commit=False)
                       data.save()
                       return redirect("app1:detail", id)
            else:
                form = CollegeForm(instance=college)
            return render(request, 'addcolleges.html', {"form": form, "controller": "Edit Colleges"})
        # if they are not admin
        else:
            return redirect("app1:home")

    # if they are not logged in
    return redirect("accounts:login")

# delete college
def delete_colleges(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            # get the colleges
            college = College.objects.get(id=id)

           # delete the college
            college.delete()
            return redirect("app1:home")
        # if they are not admin
        else:
           return redirect("app1:home")

    # if they are not logged in
    return redirect("accounts:login")

            


