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

def perfil(request):
    return render (request,'perfil.html')
def dados(request):
    context = {
        'nome': 'João',
        'idade': 16,
        'cidade': 'Teresina'
    }
    return render(request,'dados.html',context)
def form(request):
    if request.method == "POST": 
        # captura cada informação digitada no formulário
        nome = request.POST.get("Nome Completo")
        DATA = request.POST.get("Data de Nascimento")
        RG = request.POST.get("RG")
        CPF = request.POST.get("CPF")
        telefone = request.POST.get("Telefone")
        email = request.POST.get("Email")
        rua = request.POST.get("Rua")
        numero = request.POST.get("Numero")
        bairro = request.POST.get("Bairro")
        cidade = request.POST.get("Cidade")
        estado = request.POST.get("Estado")
        CEP = request.POST.get("CEP")
        # cria um dicionário context com os dados capturados
        context = {
            'nome': nome,
            'DATA': DATA,
            'RG': RG,
            'CPF': CPF,
            telefone: telefone,
            email: email,
            rua: rua,
            numero: numero,
            bairro: bairro,
            cidade: cidade,
            estado: estado,
            CEP: CEP
        }
        # mostra os dados capturados no template dados.html
        return render(request,'dados.html',context)
    else: # method GET, mostra o formulário vazio
        return render(request,'form.html')
