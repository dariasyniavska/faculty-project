from django.shortcuts import render, get_object_or_404
from .models import HomePageContent, Specialty, Department


def home_view(request):
    hp_content = HomePageContent.objects.first()
    text = hp_content.content if hp_content else "Ласкаво просимо на сайт Факультету соціальних наук та соціальних технологій НаУКМА!"
    return render(request, 'fsnst_app/home.html', {'text': text})


def programs_list_view(request):
    specialties = Specialty.objects.all()
    return render(request, 'fsnst_app/programs_list.html', {'specialties': specialties})


def program_detail_view(request, pk):
    specialty = get_object_or_404(Specialty, pk=pk)
    disciplines_list = specialty.disciplines.split('\n') if specialty.disciplines else []
    return render(request, 'fsnst_app/program_detail.html',
                  {'specialty': specialty, 'disciplines_list': disciplines_list})


def departments_list_view(request):
    departments = Department.objects.all()
    return render(request, 'fsnst_app/departments_list.html', {'departments': departments})


def department_detail_view(request, pk):
    department = get_object_or_404(Department, pk=pk)
    return render(request, 'fsnst_app/department_detail.html', {'department': department})


