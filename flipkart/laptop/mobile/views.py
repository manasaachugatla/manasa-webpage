from django.shortcuts import render

# Create your views here.
def dell(request):
    return render(request,"dell.html")
def hp(request):
    return render(request,"hp.html")