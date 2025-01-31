from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("A view funcionou")

def sobre(request):
    return HttpResponse("<h1> Sistema 1.0 desenvolvido por mim </h1>")

def contato(request):
    return HttpResponse("<h1> esta é a página de contato</h1>")

def ajuda(request):
    return HttpResponse("<h1>Esta é  a página de ajuda </h1>")

from django.shortcuts import HttpResponse
def index(request):
    return render (request,'index.html')

def sobre(request):
    return render (request,'sobre.html')

def contato(request):
    return render (request,'contato.html')

def ajuda(request):
    return render (request,'ajuda.html')

def local(request):
    return render (request,'local.html')

def exibiritem(request,id):
    return render (request,'exibiritem.html',{'id':id})