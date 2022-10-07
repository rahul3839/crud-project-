from unicodedata import name
from django.shortcuts import render
from django.http import JsonResponse
from .forms import Regstaration
from .models import RegstrationModel

# Create your views here.


def home(request):
    fm = Regstaration()
    data = RegstrationModel.objects.all()
    return render(request,'home.html',{'data':data,'form':fm})

def save_data(request):
    if request.method == 'POST':
        fm = Regstaration(request.POST)
        if fm.is_valid():
            sid = request.POST.get('stuid')
            name = request.POST['name']
            last_name = request.POST['last_name']
            if (sid == ''):
                reg = RegstrationModel(name=name,last_name=last_name)
            else:
                reg = RegstrationModel(id=sid,name=name,last_name=last_name)
            reg.save()
            stud = RegstrationModel.objects.values()
            student_data = list(stud)
            # print(student_data)
            return JsonResponse({'status':'Save','student_data':student_data})
        else:
            return JsonResponse({'status':'Faild'})


def delete_data(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        print(id)
        pi = RegstrationModel.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status':'Delete'})
    else:
        return JsonResponse({'status':'Not delete'})

def edit(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        # print(id)
        student = RegstrationModel.objects.get(pk=id)
        student_data = {'id':student.id,'name':student.name,'last_name':student.last_name}
        print(student.id)
        print(student.name)
        print(student.last_name)
        return JsonResponse(student_data)