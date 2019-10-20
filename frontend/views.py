import docx
from django.shortcuts import render
from django.http import HttpResponse
from utilits.doc_parser import DocParser


def index(request):
    return render(request, 'index.html')


def send_file(request):
    doc = docx.Document(request.FILES['file'])

    parser = DocParser()
    parser.parse_tables()

    return HttpResponse(parser.vectors)
