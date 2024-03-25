from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse

def app(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())