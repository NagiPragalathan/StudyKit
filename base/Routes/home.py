from django.shortcuts import render
from ..models import Emergency


def home(request):
    return render(request, 'front/index.html')
