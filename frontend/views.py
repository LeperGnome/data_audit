from django.shortcuts import render
from django.http import HttpResponse
import docx
from .count_services import ServiceCounter
import numpy as np

def index(request):
    return render(request, 'index.html')

def send_file(request):
    Counter = ServiceCounter(k=0.6)
    doc = docx.Document(request.FILES['file'])
    service_size = Counter.count_services(doc)
    our_price = np.random.randint(1500000, 3000000)

    return render(request, 'analize.html', {'service_size': service_size, "our_price": our_price})
