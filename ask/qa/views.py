from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Question, Answer
from django.core.exceptions import ObjectDoesNotExist
from .forms import AskForm, AnswerForm

def test(request,*args,**kwargs):
    return HttpResponse('OK')

def news(request):
    qa=Question.objects.order_by('-id')
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

    return render(request,"index.html",{"page":contacts,"paginator":p})

def popular(request):
    qa = Question.objects.popular()
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
    return render(request,"index.html",{"page":contacts,"paginator":p})

def question(request,pk):
    if request.method == 'POST':
        return answer(request)
    else:
        qa = get_object_or_404(Question,id=pk)
        ans= qa.answer_set.all()
    return render(request,'question.html',{'question':qa,'answer':ans})

def Ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            post = form.save()
            url=post.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request,'ask.html',{'form':form})

def Answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            url = answer.question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm()
    return render(request,'answer.html',{'form':form})
