from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from datetime import datetime


# Create your views here.
def get_all_devices(request):
	# Create instance of object
	smart_trash = Trash.objects.all()
	return smart_trash

def home_page(request):
    today_date = str(datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))   
    devices = get_all_devices(request)
    num = int(len(devices))
    return render(request, "../templates/home.html", {'devices':devices, 'num': num, 'today_date':today_date})

