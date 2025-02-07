from django.shortcuts import render, redirect


LISTA_ALUNOS = [
    {"nome": "João Silva", "matricula": "202301", "data_nascimento": "01/01/2000", "curso": "Técnico em Informática", "turma": "208"},
    {"nome": "Maria Oliveira", "matricula": "202302", "data_nascimento": "02/02/2001", "curso": "Técnico em Informática", "turma": "208"},
    {"nome": "Carlos Souza", "matricula": "202303", "data_nascimento": "03/03/2002", "curso": "Técnico em Informática", "turma": "208"},
]
def listar_alunos(request):
    context = {
        'lista': LISTA_ALUNOS,
    }
    return render(request, 'listar_alunos.html', context)  

def editar_aluno(request, indice):
    aluno = LISTA_ALUNOS[indice]  # Obtém a referência do aluno na lista


    if request.method == "POST":
        # Atualiza diretamente os valores do dicionário aluno
        aluno['nome'] = request.POST.get("nome")
        aluno['matricula'] = request.POST.get("matricula")
        aluno['curso'] = request.POST.get("curso")
        aluno['turma'] = request.POST.get("turma")


        return redirect('listar_alunos')  # Redireciona para a lista de alunos


    context = {
        'aluno': aluno,
        'indice': indice
    }
    return render(request, 'form_aluno.html', context)

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

from django.shortcuts import render
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
        nome = request.POST.get("nome")
        DATA = request.POST.get("DATA")
        RG = request.POST.get("RG")
        CPF = request.POST.get("CPF")
        telefone = request.POST.get("telefone")
        email = request.POST.get("email")
        rua = request.POST.get("rua")
        numero = request.POST.get("numero")
        bairro = request.POST.get("bairro")
        cidade = request.POST.get("cidade")
        estado = request.POST.get("estado")
        CEP = request.POST.get("CEP")
        # cria um dicionário context com os dados capturados
        context = {
            'nome': nome,
            'DATA': DATA,
            'RG': RG,
            'CPF': CPF,
            'telefone': telefone,
            'email': email,
            'rua': rua,
            'numero': numero,
            'bairro': bairro,
            'cidade': cidade,
            'estado': estado,
            'CEP': CEP
        }
        # mostra os dados capturados no template dados.html
        return render(request,'dados.html',context)
    else: # method GET, mostra o formulário vazio
        return render(request,'form.html')

     

