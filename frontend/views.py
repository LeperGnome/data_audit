from django.shortcuts import render
from django.http import HttpResponse
import docx


def index(request):
    return render(request, 'index.html')

def send_file(request):
    doc = docx.Document(request.FILES['file'])
    print(doc.tables[0].cell(0, 0).text)
    return HttpResponse(doc)
