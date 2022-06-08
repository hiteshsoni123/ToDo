from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from app1.models import TodosModel


def add(request):
    return render(request, "home.html")

def add_task(request):
    txt = request.POST.get('t1')
    sm = TodosModel(td = txt)
    sm.save()
    messages.success(request, "Task Added Successfully")
    return redirect('add')

def view_list(request):
    st = TodosModel.objects.all()
    return render(request, "home.html", {"data": st})

# def show(request):
#     st = TodosModel.objects.all()
#     return render(request,"home.html",{"data": st})


def del_list(request):
    var = request.GET.get("no")
    TodosModel.objects.filter(td=var).delete()
    stu = TodosModel.objects.all()
    return render(request,'home.html',{'data': stu})

