from django.shortcuts import render
from .models import Grades
# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("hell0 my first!")
def detail(request,num):
    return HttpResponse("detail-%s"%num)
def grades(request):
    #去模板里面娶数据
    gradeslist=Grades.objects.all()
    #将数据传递给模板，模板渲染页面，渲染好的页面返回给浏览器
    return render(request,'demo01/grades.html',{"grades":gradeslist})