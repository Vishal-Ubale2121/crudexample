from django.shortcuts import render, redirect,HttpResponse
from employee.forms import EmployeeForm
from django.views import View
from employee.models import Employee
from employee.forms import DocumentForm
from .models import Post
from django.forms import modelformset_factory
from .forms import PostModelForm
from rest_framework import  generics

import json

class MyForm(View):

    def post(self,request):
        if request.method == "POST":
            form = EmployeeForm(request.POST)
            if form.is_valid():
                try:
                    form.save()
                    return redirect('/show')
                except:
                    pass
        else:
            form = EmployeeForm()
        return render(request,'index.html',{'form':form})


class Model_Form(View):

    form_class = DocumentForm
    template_name = 'upload.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                with open('media\documents\person.json', 'r') as f:
                    distros_dict = json.load(f)
                    car_dict = {}
                    for v in distros_dict.values():
                        ctr = 1
                        for each in v:
                            final = (each['Car'], '------', each['Colour'], '----------------------',
                                     each['Prise'], '-------------------', each['Model'])
                            print(final)
                            car_dict['car{}'.format(ctr)] = each
                            ctr += 1
                            # context = {'rooms': final}
                        print(car_dict)
                        return render(request, 'json.html',context={"car_dict": car_dict})



        else:
            form = DocumentForm()
        return render(request, 'upload.html', {
            'form': form
        })


class ShowTable(View):

    def get(self,request):
        employees = Employee.objects.all()
        return render(request, "show.html", {'employees': employees})

    def post(self, request):
        form = self.Employee(request.POST)
        if form.is_valid():
            form.save()
            return render('/index')

        form = Employee.objects.all()
        return render(request, self.show, {'form': form})




class Delete(View):

    def get(self,request, id):
        employee = Employee.objects.get(id=id)
        employee.delete()
        return redirect("/show")

    def post(self, request):
        form = self.Employee(request.POST)
        if form.is_valid():
            form.save()
            return render('/index')

        form = Employee.objects.all()
        return render(request, self.show, {'form': form})



class Home_View(View):

    def get(self,request):
        employees = Employee.objects.all()
        return render(request,"start.html",{'employees':employees})

    def post(self, request):
        form = self.Employee(request.POST)
        if form.is_valid():
            form.save()
            return render('/index')

        form = Employee.objects.all()
        return render(request, self.show, {'form': form})




class Upload_File(View):

    def get(request):
        employees = Employee.objects.all()
        return render(request,"upload.html",{'employees':employees})

    def post(self, request):
        form = self.Employee(request.POST)
        if form.is_valid():
            form.save()
            return render('/index')

        form = Employee.objects.all()
        return render(request, self.upload, {'form': form})

    def navbar(request):
        employees = Employee.objects.all()
        return render(request, "navbar.html", {'employees': employees})

class Formset(View):

    def get(self,request):

        PostModelFormset = modelformset_factory(Post, form=PostModelForm)
        formset = PostModelFormset(request.POST or None, queryset=Post.objects.all())
        context = {'formset': formset}
        return render(request, 'formset.html', context)


    def post(self,request):
        PostModelFormset = modelformset_factory(Post, form=PostModelForm)
        formset = PostModelFormset(request.POST or None, queryset=Post.objects.all())

        if formset.is_valid():
            for form in formset:
                obj = form.save(commit=False)
                if form.cleaned_data:
                    obj.save()
        context = {'formset': formset}
        return render(request, 'formset.html', context)
