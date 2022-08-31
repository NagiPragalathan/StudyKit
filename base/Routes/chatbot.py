from django.shortcuts import render
from ..modules.Courses import cource


def cource(request):
    return render(request, 'cources/school_education/simple.html')
