from django.http import HttpResponse
from django.shortcuts import render
def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')
    removepunc=request.GET.get('removepunc','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''#whatever text will be written in the text area this program
        #will remive all the puntuations after clicking on "on" in checkbox
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)#and will take to analyze.html page

    else:
        return HttpResponse('Error')
def index(request):
    return render(request,'index.html')#it will take us to index.html