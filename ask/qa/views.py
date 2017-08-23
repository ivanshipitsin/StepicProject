from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Question
from django.core.exceptions import ObjectDoesNotExist

def test(request,*args,**kwargs):
    return HttpResponse('OK')

def news(request):
    qa=Question.objects.new()
    limit=10
    page = request.GET.get('page')
    p=Paginator(qa,limit)
    p.baseurl = '/?page='
    try:
        contacts = p.page(page)
    except PageNotAnInteger:
        contacts = p.page(1)
    except EmptyPage:
        contacts = p.page(p.num_pages)

    return render(request,"index.html",{"question":qa,"page":contacts,"paginator":p})

def popular(request):
    qa = Question.objetcs.popular()
    limit = 10
    page = request.GET.get('page')
    p=Paginator(qa,limit)
    p.baseurl = '/popular/?page='
    try:
        contacts = p.page(page)
    except PageNotAnInteger:
        contacts = p.page(1)
    except EmptyPage:
        contacts = p.page(p.num_pages)
    return render(request,"index.html",{"question":qa,"page":contacts,"paginator":p})

def question(request,pk):
    qa = get_object_or_404(Question,id=pk)
    ans= qa.anwer_set.all()
    return render(request,'question.html',{'question':qa,'answer':ans})
