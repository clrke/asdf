from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from . import ctrls

def home(request): 	return render(request, "index.html", 	ctrls.home(request))
def home2(request): return render(request, "index.html", 	ctrls.home2(request))
