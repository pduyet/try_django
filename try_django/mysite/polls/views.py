from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question

# Create your views here.

def index(request):
    myname = 'DuyetPham'
    mydomain = ["Money", "Mobile", "Laptop", "Girl Friend"]
    context = {'name': myname, 'domain':mydomain}
    return render(request, 'polls/index.html', context)

def viewquestionlist(request):
    #get_object_or_404(Question, question_text ="Ban thich mau gi"
    list_question = Question.objects.all()
    context = {'listquestion': list_question}
    return render(request, 'polls/question_list.html', context)

def detailView(request, question_id):
    q = Question.objects.get(pk=question_id)
    return render(request, "polls/detail_question.html", {"qs": q})

def vote(request, question_id):
    q = Question.objects.get(pk=question_id)
    try:
        dulieu = request.POST['choice']
        c = q.choice_set.get(pk=dulieu)
    except:
        HttpResponse('Error No have choice')
    c.vote = c.vote + 1
    c.save()
    return render(request, "polls/result.html", {"q":q})
