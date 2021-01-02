#I have created this view file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return(render(request, 'index.html'))

def analyze(request):
    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')   #prints the input give(text)
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    #analyzed = djtext
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for i in djtext:
            if i not in punctuations:
                analyzed = analyzed + i
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        #return(render(request, 'analyze.html', params))
    if fullcaps == "on":
        analyzed = ""
        for i in djtext:
                analyzed = analyzed + i.upper()
        params = {'purpose': 'Upper Case', 'analyzed_text': analyzed}
        djtext = analyzed
        #return(render(request, 'analyze.html', params))
    if newlineremover == "on":
        analyzed = ""
        for i in djtext:
            if i != "\n" and i != "\r":
                analyzed = analyzed + i
        params = {'purpose': 'Remove Line', 'analyzed_text': analyzed}
        djtext = analyzed
        #return(render(request, 'analyze.html', params))
    if extraspaceremover == "on":
        analyzed = ""
        for index,char in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Extra Spce Removed', 'analyzed_text': analyzed}
        djtext = analyzed
        #return(render(request, 'analyze.html', params))
    if charcount == "on":
        count = 0
        for i in djtext:
            if i != ' ' and i != "\n" and i != "\r":
                count = count + 1
        params = {'purpose': 'Character Counted', 'analyzed_text': count}
        #return(render(request, 'analyze.html', params))
    if removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcount != "on":
        return(HttpResponse('Error'))
    
    return(render(request, 'analyze.html', params))