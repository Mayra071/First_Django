from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, world! \n You are in home page of Chai aur Code")
    return render(request, 'website/index.html')

def about(request):
    # return HttpResponse("Hello, world! \n You are in about page of Chai aur Code")
    return render(request, 'website/about.html')

def contact(request):
    # return HttpResponse("Hello, world! \n You are in contact page of Chai aur Code")
    return render(request,'manish.html')
