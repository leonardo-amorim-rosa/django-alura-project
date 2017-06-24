from django.shortcuts import render, redirect
from perfis.models import Perfil, Convite
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseForbidden
# from django.http import HttpResponse


@login_required
@require_http_methods(['GET'])
def index(request):
    print request.user.username #novo
    print request.user.email #novo
    print request.user.has_perm('perfis.add_convite') #novo

    return render(request, 'index.html', {'perfis': Perfil.objects.all(), 'perfil_logado': get_perfil_logado(request)})
    # return HttpResponse('Bem vindo ao Django!!!')


@login_required
def exibir(request, perfil_id):

    '''
        perfil = Perfil()
        if perfil_id == '1':
            perfil = Perfil('teste', 'test@mail.com', '2212121212', 'empresa_teste')
    '''

    perfil = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    ja_eh_logado = perfil in perfil_logado.contatos.all()
    return render(request, 'perfis.html', {"perfil": perfil, "ja_eh_logado" : ja_eh_logado})


@login_required
# @permission_required('perfis.add_convite', raise_exception=True)
def convidar(request, perfil_id):

    if not request.user.has_perm('perfis.add_convite'):
        return HttpResponseForbidden('Acesso negado')    

	perfil_a_convidar = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(request)
	perfil_logado.convidar(perfil_a_convidar)
	return redirect('index')


@login_required
def get_perfil_logado(request):
	return request.user.perfil	


@login_required
def aceitar(request, convite_id):
	convite = Convite.objects.get(id=convite_id)
	convite.aceitar()
	return redirect('index')	