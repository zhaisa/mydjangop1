from django.shortcuts import render
from .models import Grades,Students,Blog,Blogcon,Dreamreal
# Create your views here.
from django.http import HttpResponse
import datetime
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
def rongbeitask(request):
    return render(request,'demo01/rongbeitask.html')
def hello(request):
    # text = "<h1>welcome to my app number %s!</h1>"
    today = datetime.datetime.now().date()
    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return render(request,'demo01/hello.html',{"today":today.isoformat(), "days_of_week" : daysOfWeek})


def crudops(request):
    # Creating an entry

    dreamreal = Dreamreal(
        website="www.polo.com", mail="sorex@polo.com",
        name="sorex", phonenumber="002376970"
    )

    dreamreal.save()

    # Read ALL entries
    objects = Dreamreal.objects.all()
    res = 'Printing all Dreamreal entries in the DB : <br>'

    for elt in objects:
        res += elt.name + "<br>"

    # Read a specific entry:
    sorex = Dreamreal.objects.get(name="sorex")
    res += 'Printing One entry <br>'
    res += sorex.name

    # Delete an entry
    res += '<br> Deleting an entry <br>'
    sorex.delete()

    # Update
    dreamreal = Dreamreal(
        website="www.polo.com", mail="sorex@polo.com",
        name="sorex", phonenumber="002376970"
    )

    dreamreal.save()
    res += 'Updating entry<br>'

    dreamreal = Dreamreal.objects.get(name='sorex')
    dreamreal.name = 'thierry'
    dreamreal.save()

    return HttpResponse(res)


def datamanipulation(request):
    res = ''

    # Filtering data:
    qs = Dreamreal.objects.filter(name="paul")
    res += "Found : %s results<br>" % len(qs)

    # Ordering results
    qs = Dreamreal.objects.order_by("name")

    for elt in qs:
        res += elt.name + '<br>'

    return HttpResponse(res)