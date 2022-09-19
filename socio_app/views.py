from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import HttpResponse
from . forms import RegistrationForm, NewServiceForm, QueriesForm, AnswerForm
from .models import AddService, Queries, Answers
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.

def homepage(request):
    #return HttpResponse("hi")
    return render(request,'main/index.html')

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request,'registration/register.html',{'form':form})

@login_required
def post_service(request):
    form = NewServiceForm()
    if request.method == 'POST':
        form = NewServiceForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('homepage')
    else:
        form = NewServiceForm()
    return render(request,'services/addservice.html',{'form_data':form})

@login_required
def webdesign_list(request):
    post = AddService.objects.all()
    result={'post':post}
    return render(request,'services/webdesign.html',result)

@login_required
def videoediting_list(request):
    post = AddService.objects.all()
    result={'post':post}
    return render(request,'services/videoediting.html',result)

@login_required
def uidesign_list(request):
    post = AddService.objects.all()
    result={'post':post}
    return render(request,'services/uidesign.html',result)

@login_required
def it_list(request):
    post = AddService.objects.all()
    result={'post':post}
    return render(request,'services/it.html',result)

@login_required
def account_list(request):
    post = AddService.objects.all()
    result={'post':post}
    return render(request,'services/account.html',result)

@login_required
def photoediting_list(request):
    post = AddService.objects.all()
    result={'post':post}
    return render(request,'services/photoediting.html',result)

@login_required
def queries(request):
    form = QueriesForm()
    if request.method == 'POST':
        form = QueriesForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('query_list')
    else:
        form = QueriesForm()
    return render(request,'queries/addquery.html',{'query_form':form})


@login_required
def query_list(request):
    if 'query' in request.GET:
        query = request.GET['query']
        query_post = Queries.objects.filter(question__icontains=query).order_by('-id')
    else:
        query_post = Queries.objects.filter(create_date__lte=timezone.now()).order_by('-create_date', '-create_time')
    result1={'query_post':query_post}
    return render(request,'queries/queries.html',result1)

def query_detail(request, pk):
    query = Queries.objects.get(pk=pk)
    answer = Answers.objects.filter(questions=query)
    answer_form = AnswerForm()
    if request.method == 'POST':
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            ans = answer_form.save(commit=False)
            ans.questions=query
            ans.save()
            return redirect('query_detail',pk=pk)
    else:
        form = AnswerForm()
    return render(request, 'queries/query_detail.html', {'query': query,'answer':answer,'answer_form':answer_form})
