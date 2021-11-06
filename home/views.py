from django.http.response import HttpResponse
from django.shortcuts import render
from home.models import Converter

# Create your views here.
def home(request):
    return render(request,'index.html')
# punctuation
# captialise
# smallise
# new line character remove
# remove extra space
# counct characters
# count words
def result(request):
    text=request.POST['para']
    punc=request.POST.get('removepunc','off')
    uppercase=request.POST.get('uppercase','off')
    lowercase=request.POST.get('lowercase','off')
    countchar=request.POST.get('countchar','off')
    countwords=request.POST.get('countwords','off')
    removenewline=request.POST.get('removenewline','off')
    listofpunc='''~!@#$%^&*()_[]:"'<>?/\/.,;=-+|'''
    analyzeddata=""
    if punc=='on':
        for char in text:
            if char not in listofpunc:
                analyzeddata+=char
        context={'purpose':'Remove all Punctuations symbol ','data':analyzeddata}
        text=analyzeddata
    if uppercase=='on':
        analyzeddata=text.upper()
        # for char in text:
        #     analyzeddata+=char.upper()
        context={'purpose':'All data in uppercase','data':analyzeddata}
        text=analyzeddata
    if lowercase=='on':
        analyzeddata=text.lower()
        context={'purpose':'All data in lowercase','data':analyzeddata}
        text=analyzeddata
    if countchar=='on':
        length=len(text)
        context={'purpose':'Count all character in data','data':length}
    if countwords=='on':
        words=text.split()
        length=len(words)
        context={'purpose':'Count all words in data','data':length}
    if removenewline=='on':
        for char in text:
            if(char!='\n' and char!='\r'):
                 analyzeddata+=char
        context={'purpose':'POSTemove new line','data':analyzeddata} 
    return render(request,'result.html',context)


        
        
