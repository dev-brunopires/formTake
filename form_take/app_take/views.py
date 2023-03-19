from django.shortcuts import render

from .models import registros


# Create your views here.
def formularios(request):
    return render(request, 'formulario/index.html')


def lists(resquest):

    # Salvar os dados da tela no banco de dados
    novo_registro = registros()
    novo_registro.nome = resquest.POST.get("nome")
    novo_registro.idade = resquest.POST.get("idade")

    novo_registro.save()

    # Exibir todos registros cadastrados em uma nova pagina

    newRegister = {
        "registros": registros.objects.all()
    }

    return render(resquest, 'registros/index.html', newRegister)
