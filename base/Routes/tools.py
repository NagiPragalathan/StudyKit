from django.shortcuts import render
from ..modules import Tools

def TexttoSound(request):
    return render(request, 'tools/TextToVoice.html')

def ToolMenu(request):
    return render(request, 'tools/listout.html')

def KeywordToPara(request):
    return render(request, 'tools/KeywordToPara.html')

def KeyWordToText(request):
    return render(request, 'tools/KeyWordToText.html')

def KeyWordToAudio(request):
    return render(request, 'tools/KeyWordToAudio.html')

def TexttoHandWritten(request):
    return render(request, 'tools/HandToText.html')

def Dictinary(request):
    return render(request, 'tools/dic.html')

def KeyWordToImage(request):
    return render(request, 'tools/KeyWordToImage.html')


