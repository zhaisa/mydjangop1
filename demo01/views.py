from django.shortcuts import render
from .models import Grades,Students,Blog,Blogcon
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
def stydents(request):
    #去模板里面娶数据
    studentslist=Students.objects.all()
    #将数据传递给模板，模板渲染页面，渲染好的页面返回给浏览器
    return render(request,'demo01/students.html',{"students":studentslist})
def gradesstudets(request,num):
    #获得对应班级对象
    grade=Grades.objects.get(pk=num)
    #获得队友班级下的学生
    studentlist=grade.students_set.all()
    return  render(request,'demo01/students.html',{"students":studentlist})
def blog(request):
    bloglist=Blog.objects.all()
    return render(request,'demo01/blog.html',{"blogs":bloglist})
def blogco(request):
    blogcolist=Blogcon.objects.all()
    return render(request,'demo01/blogco.html',{"blogcos":blogcolist})