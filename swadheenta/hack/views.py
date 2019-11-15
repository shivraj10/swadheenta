from django.http import HttpResponse
from django.shortcuts import render

def show(request):
    return render(request,'hack/index.html')

