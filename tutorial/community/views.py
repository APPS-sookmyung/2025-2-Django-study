from django.shortcuts import render
from community.forms import *

# Create your views here.
def write(request):
    if request.method == 'POST': #폼이 제출되었을 때
        form = Form(request.POST) #폼 객체 생성
        if form.is_valid(): #폼이 유효한지 검사
            form.save() #폼 데이터를 저장
        else: #폼이 제출되지 않았을 때
            form = Form() #빈 폼 객체 생성  
    form = Form()
    return render(request, 'write.html', {'form': form}) #html에 폼을 전달한다. 

def list(request):
    articleList = Article.objects.all() #모든 글을 가져온다.
    return render(request, 'list.html', {'articleList':articleList}) #html에 데이터를 전달한다.

def view(request, num=1):
    article = Article.objects.get(id=num) #num에 해당하는 글을 가져온다.
    return render(request, 'view.html', {'article':article}) #html에 데이터를 전달한다.