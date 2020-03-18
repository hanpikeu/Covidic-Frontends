from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

def index(request):
  return render(request, 'main/index.html')

def cg_timeline(request):
    return render(request, 'chinagate/chinagate-time.html')

def cg_ar(request):
    return render(request, 'chinagate/chinagate-ar.html')

def cg_fact(request):
    return render(request, 'chinagate/chinagate-fact.html')



