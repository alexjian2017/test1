from django.http import HttpResponse
from django.shortcuts import render
def hello(request):
    return HttpResponse('what the fuck')

def index(request):
    context = {}
    context['name'] = '程序員阿源'

    return render(request, 'index.html',context)

def index1(request):
    context = {}

    # variable
    context['name'] = '程序員阿原'

    # list
    view_list = ['hihi','What the fuck', 'OMG']
    context['view_list'] = view_list

    # dictionary
    view_dic = {'name': '程序員阿原', 'age':'27'}
    context['view_dic'] = view_dic

    # empty list
    empty_list = []
    context['empty_list'] = empty_list

    #if/else
    score = 20
    context['score'] = score

    return render(request, 'index1.html',context)