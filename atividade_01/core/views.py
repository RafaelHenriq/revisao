from django.shortcuts import render

def nome(request):
    return render(request, 'nome.html')

def home(request):
    return render(request, 'index.html')    

def ifrn(request):
    return render(request, 'campus.html')    

    

    
