import requests
from .shortcuts import compact

def home(request):
	activities = requests.get('http://student-journal.eu1.frbit.net/activities').json()
	message = "Hello one"

	return compact('activities', 'message')

def home2(request):
	activities = requests.get('http://student-journal.eu1.frbit.net/activities').json()
	message = "Hello two"

	return compact('activities', 'message')

