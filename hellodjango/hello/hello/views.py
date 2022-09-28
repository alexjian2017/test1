from django.http import HttpResponse
from django.shortcuts import render
def hello(request):
    return HttpResponse('what the fuck')

def index(request):
    context = {}
    context['name'] = '程序員阿源'
    return render(request, 'index.html',context)