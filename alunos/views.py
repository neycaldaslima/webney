import email

from django.http import request
from django.shortcuts import redirect, render
from .models import Aluno


def listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/listar.html', {'alunos': alunos})


def cadastrar(request):
    if request.method == 'POST':
        cpf = request.POST['cpf']
        matricula = request.POST['matricula']
        if Aluno.objects.filter(cpf=cpf).exists():
            return render(request, 'alunos/cadastrar.html', {
                'erro': 'Este CPF já está cadastrado.'
            })
        if Aluno.objects.filter(matricula=matricula).exists():
            return render(request, 'alunos/cadastrar.html', {
                'erro': 'Esta matrícula já está cadastrada.'
            })
        nome = request.POST['nome']
        idade = request.POST.get('idade') or None
        email = request.POST['email']
        telefone = request.POST['telefone']
        endereco = request.POST['endereco']
        aluno = Aluno(cpf=cpf, matricula=matricula, nome=nome, idade=idade, email=email, telefone=telefone, endereco=endereco)
        aluno.save()
        return redirect('listar_alunos')
    return render(request, 'alunos/cadastrar.html') 

# Create your views here.
