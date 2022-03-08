from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    return render(request,'login.html');

def home_page(request):
    return render(request,'homepage.html');

def dashboard(request):
    return render(request,'dashboard.html');
    
def studentdetail(request):
    return render(request,'student_details.html');

def feedetail(request):
    return render(request,'FeesDetails.html');


def drivedetail(request):
    return render(request,'placements.html');