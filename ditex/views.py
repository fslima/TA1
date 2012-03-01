# -*- coding:utf-8 -*-
#from utils import *
from response import JSONResponse
import urllib, json

from datetime import datetime, date, timedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from models import *
from django.template import RequestContext
from forms import *

def sair(request):
	logout(request)
	return HttpResponseRedirect("/login")

@login_required
def inicio(request):
	data = datetime.now()
	return render_to_response('inicio.html', locals())

def exibe(request, objeto, id_objeto):
	if str(objeto) == 'aluno':
		titulo = 'Aluno'
		objeto = get_object_or_404(Aluno, pk = id_objeto)
		form = FormAluno(instance = objeto)
	if str(objeto) == 'curso':
		titulo = 'Curso'
		objeto = get_object_or_404(Curso, pk = id_objeto)
		form = FormCurso(instance = objeto)
	if str(objeto) == 'empresa':
		titulo = 'Empresa'
		objeto = get_object_or_404(Empresa, pk = id_objeto)
		form = FormEmpresa(instance = objeto)
	if str(objeto) == 'oportunidade':
		titulo = 'Oportunidade'
		objeto = get_object_or_404(Oportunidade, pk = id_objeto)
		membros = objeto.curso.all
		empresa = objeto.empresa
		titulo_membros = 'Cursos Relacionados à Vaga'
		form = FormOportunidade(instance = objeto)
	if str(objeto) == 'encaminhamento':
		titulo = 'Encaminhamento'
		objeto = get_object_or_404(Encaminhamento, pk = id_objeto)
		form = FormEncaminhamento(instance = objeto)
	if str(objeto) == 'evento':
		titulo = 'Evento'
		objeto = get_object_or_404(Evento, pk = id_objeto)
		membros = objeto.participante.all
		titulo_membros = 'Participantes Inscritos'
		form = FormEvento(instance = objeto)
	return render_to_response('exibe.html', locals())

@login_required
def adiciona(request, objeto):
	if str(objeto) == 'aluno':
		titulo = 'Aluno'
		formpost = FormAluno(request.POST, request.FILES)
		formget = FormAluno()
	if str(objeto) == 'curso':
		titulo = 'Curso'
		formpost = FormCurso(request.POST, request.FILES)
		formget = FormCurso()	
	if str(objeto) == 'empresa':
		titulo = 'Empresa'
		formpost = FormEmpresa(request.POST, request.FILES, )
		formget = FormEmpresa()	
	if str(objeto) == 'oportunidade':
		titulo = 'Oportunidade'
		formpost = FormOportunidade(request.POST, request.FILES)
		formget = FormOportunidade()	
	if str(objeto) == 'evento':
		titulo = 'Evento'
		formpost = FormEvento(request.POST, request.FILES)
		formget = FormEvento()
	if str(objeto) == 'encaminhamento':
		titulo = 'Encaminhamento'
		formpost = FormEncaminhamento(request.POST, request.FILES)
		formget = FormEncaminhamento()
	if request.method == 'POST': 
		form = formpost
		if form.is_valid():
			objeto_form = form.save(commit = False)
			objeto_form.usuario = request.user
			if objeto_form.validaAtrib() != 'validos':
				erro =  objeto_form.validaAtrib()
				return render_to_response("adiciona.html", locals(), context_instance = RequestContext(request))
			objeto_form.save()
			return HttpResponseRedirect("/lista/"+str(objeto))
		else:
			return render_to_response("adiciona.html", locals(), context_instance = RequestContext(request))
	else: 
		form = formget
		return render_to_response("adiciona.html", locals(), context_instance = RequestContext(request))
	
@login_required
def edita(request, objeto, id_objeto):
	if str(objeto) == 'aluno':
		aluno_para_editar = get_object_or_404(Aluno, pk = id_objeto)
		formpost = FormAluno(request.POST, request.FILES, instance = aluno_para_editar)
		formget = FormAluno(instance = aluno_para_editar)
		titulo = 'Aluno'		
	if str(objeto) == 'curso':
		titulo = 'Curso'
		curso_para_editar = get_object_or_404(Curso, pk = id_objeto)
		formpost = FormCurso(request.POST, request.FILES, instance = curso_para_editar)
		formget = FormCurso(instance = curso_para_editar)	
	if str(objeto) == 'empresa':
		titulo = 'Empresa'
		empresa_para_editar = get_object_or_404(Empresa, pk = id_objeto)
		formpost = FormEmpresa(request.POST, request.FILES, instance = empresa_para_editar)
		formget = FormEmpresa(instance = empresa_para_editar)	
	if str(objeto) == 'oportunidade':
		titulo = 'Oportunidade'
		oportunidade_para_editar = get_object_or_404(Oportunidade, pk = id_objeto)
		formpost = FormOportunidade(request.POST, request.FILES, instance = oportunidade_para_editar)
		formget = FormOportunidade(instance = oportunidade_para_editar)	
	if str(objeto) == 'cursosdaoportunidade':
		objeto = 'oportunidade'
		titulo = 'Curso'
		oportunidade_para_editar = get_object_or_404(Oportunidade, pk = id_objeto)
		formpost = FormCursoOportunidade(request.POST, request.FILES, instance = oportunidade_para_editar)
		formget = FormCursoOportunidade(instance = oportunidade_para_editar)
	if str(objeto) == 'evento':
		titulo = 'Evento'
		evento_para_editar = get_object_or_404(Evento, pk = id_objeto)
		formpost = FormEvento(request.POST, request.FILES, instance = evento_para_editar)
		formget = FormEvento(instance = evento_para_editar)
	if str(objeto) == 'participantesdoevento':
		objeto = 'evento'
		titulo = 'Participante'
		evento_para_editar = get_object_or_404(Evento, pk = id_objeto)
		formpost = FormParticipante(request.POST, request.FILES, instance = evento_para_editar)
		formget = FormParticipante(instance = evento_para_editar)
	if str(objeto) == 'encaminhamento':
		titulo = 'Encaminhamento'
		encaminhamento_para_editar = get_object_or_404(Encaminhamento, pk = id_objeto)
		formpost = FormEncaminhamento(request.POST, request.FILES, instance = encaminhamento_para_editar)
		formget = FormEncaminhamento(instance = encaminhamento_para_editar)	
	if request.method == 'POST':
		form = formpost
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/lista/"+str(objeto))
		else:
			return render_to_response('edita.html', locals(), context_instance = RequestContext(request))	
	else:
		form = formget
	return render_to_response('edita.html', locals(), context_instance = RequestContext(request))

@login_required
def deleta(request, objeto, id_objeto):
	if str(objeto) == 'aluno':
		objeto_para_deletar = get_object_or_404(Aluno, pk = id_objeto)
		form = FormAluno(instance = objeto_para_deletar)
	if str(objeto) == 'curso':
		objeto_para_deletar = get_object_or_404(Curso, pk = id_objeto)
		form = FormCurso(instance = objeto_para_deletar)
	if str(objeto) == 'empresa':
		objeto_para_deletar = get_object_or_404(Empresa, pk = id_objeto)
		form = FormEmpresa(instance = objeto_para_deletar)
	if str(objeto) == 'oportunidade':
		objeto_para_deletar = get_object_or_404(Oportunidade, pk = id_objeto)
		form = FormOportunidade(instance = objeto_para_deletar)
	if str(objeto) == 'evento':
		objeto_para_deletar = get_object_or_404(Evento, pk = id_objeto)
		form = FormEvento(instance = objeto_para_deletar)
	if str(objeto) == 'encaminhamento':
		objeto_para_deletar = get_object_or_404(Encaminhamento, pk = id_objeto)
		form = FormEncaminhamento(instance = objeto_para_deletar)
	if request.method == 'POST':
		objeto_para_deletar.delete()
		return HttpResponseRedirect("/lista/"+str(objeto))
	else:
		return render_to_response('deleta.html', locals(), context_instance = RequestContext(request))
	
@login_required
def lista(request, objeto):
	if str(objeto) == 'aluno':
		titulo = 'Lista de Alunos'
		lista_vazia = 'Nenhum Aluno Cadastrado'
		lista = Aluno.objects.all().order_by('nome')
	if str(objeto) == 'curso':
		titulo = 'Lista de Cursos'
		lista_vazia = 'Nenhum Curso Cadastrado'
		lista = Curso.objects.all().order_by('nome')
	if str(objeto) == 'empresa':
		titulo = 'Lista de Empresas'
		lista_vazia = 'Nenhuma Empresa Cadastrada'
		lista = Empresa.objects.all().order_by('nome')
	if str(objeto) == 'oportunidade':
		titulo = 'Quadro de Oportunidades'
		lista_vazia = 'Nenhuma Oportunidade Aberta no Momento'
		ontem = datetime.now() - timedelta(1)
		lista = Oportunidade.objects.filter(dtfim__gt = ontem).order_by('dtfim').reverse()
	if str(objeto) == 'encaminhamento':
		titulo = 'Encaminhamentos em Aberto'
		lista_vazia = 'Nenhum Encaminhamento em Aberto'
		lista = Encaminhamento.objects.exclude(situacao = 'Concluído').order_by('dtfim').reverse()
	if str(objeto) == 'evento':
		titulo = 'Últimos Eventos Realizados'
		lista_vazia = 'Nenhum Evento Realizado'
		ontem = datetime.now() - timedelta(1)
		lista = Evento.objects.all().order_by('dtfim').reverse()[:10]
	return render_to_response('lista.html', locals())

@login_required
def filtra(request, objeto):
	if str(objeto) == 'aluno':
		titulo = 'Filtrar Aluno'
		lista_vazia = 'Nenhum Aluno Relacionado'
		lista_titulo = 'Alunos Relacionados'
		formpost = FormFiltraAluno(request.POST, request.FILES)
		formget = FormFiltraAluno()
		matricula = 'matricula'
		nome = 'nome'
		curso = 'curso'
		campos = [matricula, nome, curso]
		if request.method == 'POST':
			form = formpost
			if form.is_valid():
				parametros = []	
				valor_campo = []		
				for campo in campos:
					valor_campo.append(form.cleaned_data[campo])
					if valor_campo[-1] != '':
						parametros.append(campo)
					if valor_campo[-1] == str(0):
						parametros.pop(-1)
				matricula = valor_campo[0]
				nome = valor_campo[1]
				curso = valor_campo[2]
				if curso == str(0):
					query = Aluno.objects.filter(matricula__contains = matricula).filter(nome__icontains = nome)
					query = query.exclude(curso = curso)
				else:
					query = Aluno.objects.filter(matricula__contains = matricula).filter(nome__icontains = nome)
					query = query.filter(curso = curso)
				total = query.count()
				return render_to_response('filtra.html', locals(), context_instance = RequestContext(request))
			else:
				return render_to_response('filtra.html', locals(), context_instance = RequestContext(request))	
		else:
			form = FormFiltraAluno()
		return render_to_response('filtra.html', locals(), context_instance = RequestContext(request))
	if str(objeto) == 'curso':
		titulo = 'Filtrar Curso'
		lista_vazia = 'Nenhum Curso Relacionado'
		lista_titulo = 'Cursos Relacionados'
		formpost = FormFiltraCurso(request.POST, request.FILES)
		formget = FormFiltraCurso()
		tpcurso = 'tpcurso'
		nome = 'nome'
		campos = [tpcurso, nome]
		if request.method == 'POST':
			form = formpost
			if form.is_valid():
				parametros = []	
				valor_campo = []		
				for campo in campos:
					valor_campo.append(form.cleaned_data[campo])
					if valor_campo[-1] != '':
						parametros.append(campo)
					if valor_campo[-1] == None:
						parametros.pop(-1)
				tpcurso = valor_campo[0]
				nome = valor_campo[1]
				if tpcurso == '':
					query = Curso.objects.filter(nome__icontains = nome)
					query = query.exclude(tpcurso = tpcurso)
				else:
					query = Curso.objects.filter(nome__icontains = nome)
					query = query.filter(tpcurso = tpcurso)
				total = query.count()
				return render_to_response('filtra.html', locals(), context_instance = RequestContext(request))
			else:
				return render_to_response('filtra.html', locals(), context_instance = RequestContext(request))	
		else:
			form = FormFiltraCurso()
		return render_to_response('filtra.html', locals(), context_instance = RequestContext(request))
	if str(objeto) == 'empresa':
		titulo = 'Filtrar Empresa'
		lista_vazia = 'Nenhuma Empresa Relacionada'
		lista_titulo = 'Empresas Relacionadas'
		formpost = FormFiltraEmpresa(request.POST, request.FILES)
		formget = FormFiltraEmpresa()
		nome = 'nome'
		bairro = 'bairro'
		cidade = 'cidade'
		uf = 'uf'
		campos = [nome, bairro, cidade, uf]
		if request.method == 'POST':
			form = formpost
			if form.is_valid():
				parametros = []	
				valor_campo = []		
				for campo in campos:
					valor_campo.append(form.cleaned_data[campo])
					if valor_campo[-1] != '':
						parametros.append(campo)
					if valor_campo[-1] == None:
						parametros.pop(-1)
				nome = valor_campo[0]
				bairro = valor_campo[1]
				cidade = valor_campo[2]
				uf = valor_campo[3]
				if uf == '':
					query = Empresa.objects.filter(nome__icontains = nome).filter(bairro__icontains = bairro).filter(cidade__icontains = cidade)
					query = query.exclude(uf = uf)
				else:
					query = Empresa.objects.filter(nome__icontains = nome).filter(bairro__icontains = bairro).filter(cidade__icontains = cidade)
					query = query.filter(uf = uf)
				total = query.count()
				return render_to_response('filtra.html', locals(), context_instance = RequestContext(request))
			else:
				return render_to_response('filtra.html', locals(), context_instance = RequestContext(request))	
		else:
			form = FormFiltraEmpresa()
		return render_to_response('filtra.html', locals(), context_instance = RequestContext(request))
	if str(objeto) == 'oportunidade':
		titulo = 'Filtrar Oportunidade'
		lista_vazia = 'Nenhuma Oportunidade Relacionada'
		lista_titulo = 'Oportunidades Relacionadas'
		formpost = FormFiltraOportunidade(request.POST, request.FILES)
		formget = FormFiltraOportunidade()
		tpoportunidade = 'tpoportunidade'
		empresa = 'empresa'
		curso = 'curso'
		campos = [tpoportunidade, empresa, curso]
		if request.method == 'POST':
			form = formpost
			if form.is_valid():
				parametros = []	
				valor_campo = []		
				for campo in campos:
					valor_campo.append(form.cleaned_data[campo])
					if valor_campo[-1] != str(0):
						parametros.append(campo)
					if valor_campo[-1] == '':
						parametros.pop(-1)
				tpoportunidade = valor_campo[0]
				empresa = valor_campo[1]
				curso = valor_campo[2]
				query = Oportunidade.objects.all().order_by('dtfim').reverse()
				if tpoportunidade == '':
					query = query.exclude(tpoportunidade = tpoportunidade)
				else:
					query = query.filter(tpoportunidade = tpoportunidade)
				if empresa == str(0):
					query = query.exclude(empresa = empresa)
				else:
					query = query.filter(empresa = empresa)
				if curso == str(0):
					query = query.exclude(curso = curso)
				else:
					query = query.filter(curso = curso)
				total = query.count()
				return render_to_response('filtra.html', locals(), context_instance = RequestContext(request))
			else:
				return render_to_response('filtra.html', locals(), context_instance = RequestContext(request))	
		else:
			form = FormFiltraOportunidade()
		return render_to_response('filtra.html', locals(), context_instance = RequestContext(request))

	if str(objeto) == 'encaminhamento':
		titulo = 'Filtrar Encaminhamento'
		lista_vazia = 'Nenhum Encaminhamento Relacionado'
		lista_titulo = 'Encaminhamentos Relacionados'
		formpost = FormFiltraEncaminhamento(request.POST, request.FILES)
		formget = FormFiltraEncaminhamento()
		tpoportunidade = 'tpoportunidade'
		empresa = 'empresa'
		aluno = 'aluno'
		situacao = 'situacao'
		campos = [tpoportunidade, empresa, aluno, situacao]
		if request.method == 'POST':
			form = formpost
			if form.is_valid():
				parametros = []	
				valor_campo = []		
				for campo in campos:
					valor_campo.append(form.cleaned_data[campo])
					if valor_campo[-1] != str(0):
						parametros.append(campo)
					if valor_campo[-1] == '':
						parametros.pop(-1)
				tpoportunidade = valor_campo[0]
				empresa = valor_campo[1]
				aluno = valor_campo[2]
				situacao = valor_campo[3]
				query = Encaminhamento.objects.all().order_by('dtfim').reverse()
				if tpoportunidade == '':
					oportunidade = 0
					query = query.exclude(oportunidade = oportunidade)
				else:
					oportunidade = Oportunidade.objects.filter(tpoportunidade = tpoportunidade)
					if type(oportunidade) is list:
						query = query.filter(oportunidade__in = oportunidade)
					else:
						query = query.filter(oportunidade__in = oportunidade)
				if empresa == str(0):
					oportunidade = 0
					query = query.exclude(oportunidade = oportunidade)
				else:
					oportunidade = Oportunidade.objects.filter(empresa = empresa)
					if type(oportunidade) is list:
						query = query.filter(oportunidade__in = oportunidade)
					else:
						query = query.filter(oportunidade__in = oportunidade)
				if aluno == str(0):
					query = query.exclude(aluno = aluno)
				else:
					query = query.filter(aluno = aluno)
				if situacao == '':
					query = query.exclude(situacao = situacao)
				else:
					query = query.filter(situacao = situacao)
				total = query.count()
				return render_to_response('filtra.html', locals(), context_instance = RequestContext(request))
			else:
				return render_to_response('filtra.html', locals(), context_instance = RequestContext(request))	
		else:
			form = FormFiltraEncaminhamento()
		return render_to_response('filtra.html', locals(), context_instance = RequestContext(request))

	if str(objeto) == 'evento':
		titulo = 'Filtrar Evento'
		lista_vazia = 'Nenhum Evento Relacionado'
		lista_titulo = 'Eventos Relacionados'
		formpost = FormFiltraEvento(request.POST, request.FILES)
		formget = FormFiltraEvento()
		nome = 'nome'
		participante = 'participante'
		campos = [nome, participante]
		if request.method == 'POST':
			form = formpost
			if form.is_valid():
				parametros = []	
				valor_campo = []		
				for campo in campos:
					valor_campo.append(form.cleaned_data[campo])
					if valor_campo[-1] != str(0):
						parametros.append(campo)
					if valor_campo[-1] == '':
						parametros.pop(-1)
				nome = valor_campo[0]
				participante = valor_campo[1]
				query = Evento.objects.filter(nome__icontains = nome).order_by('dtfim').reverse()
				if participante == str(0):
					query = query.exclude(participante = participante)
				else:
					query = query.filter(participante = participante)
				total = query.count()
				return render_to_response('filtra.html', locals(), context_instance = RequestContext(request))
			else:
				return render_to_response('filtra.html', locals(), context_instance = RequestContext(request))	
		else:
			form = FormFiltraEvento()
		return render_to_response('filtra.html', locals(), context_instance = RequestContext(request))

def servico__oportunidades_abertas(request):
	ontem = datetime.now() - timedelta(1)
	oportunidades = Oportunidade.objects.filter(dtfim__gt = ontem).order_by('dtfim').reverse()
	return JSONResponse(oportunidades.values('id','vaga', 'tpoportunidade', 'empresa', 'curso', 'descoportunidade', 'dtinicio', 'dtfim', 'nrvagas'))	

def servico_exibir(request, objeto):
	if str(objeto) == 'oportunidade':
		titulo = 'Serviço Listar Oportunidades'	
		oportunidades = []
		arquivo = file('/home/fsouza/abertas')
		teste = json.load(arquivo)
		for x in range(len(teste)):
			oportunidades.append(teste[x]['id'])
		lista = Oportunidade.objects.filter(id__in = oportunidades).order_by('dtfim').reverse()
		return render_to_response('lista.html', locals())

def servico_cadastrar(request, objeto):
	if str(objeto) == 'oportunidade':
		arquivo = file('/opt/tpcavancados/jsonoportunidade')
		teste = json.load(arquivo)
		oportunidade = Oportunidade(
				vaga = teste[0]['vaga'], tpoportunidade = teste[0]['tpoportunidade'],
				empresa = Empresa.objects.get(pk = teste[0]['empresa']),
				descoportunidade = teste[0]['descoportunidade'],
				dtinicio = teste[0]['dtinicio'],
				dtfim = teste[0]['dtfim'],
				nrvagas = teste[0]['nrvagas'],
				usuario = User.objects.get(pk = 1))
		oportunidade.save()
		return HttpResponseRedirect("/lista/"+str(objeto))
	if str(objeto) == 'participante':
		arquivo = file('/opt/tpcavancados/jsonevento')
		teste = json.load(arquivo)
		evento = Evento.objects.get(pk = teste[0]['evento'])
		participante = Aluno.objects.get(pk = teste[0]['participante'])
		evento.participante.add(participante)
		evento.save()
		return HttpResponseRedirect("/exibe/evento/"+str(teste[0]['evento']))
	if str(objeto) == 'curso':
		arquivo = file('/opt/tpcavancados/jsoncurso')
		teste = json.load(arquivo)
		for x in range(len(teste)):
			curso = Curso(
				tpcurso = teste[x]['tpcurso'],
				nome = teste[x]['nome'],
				nrperiodos = teste[x]['nrperiodos'])
			curso.save()
		return HttpResponseRedirect("/lista/"+str(objeto))
	if str(objeto) == 'aluno':
		arquivo = file('/opt/tpcavancados/jsonaluno')
		teste = json.load(arquivo)
		for x in range(len(teste)):
			aluno = Aluno(
				matricula = teste[x]['matricula'],
				nome = teste[x]['nome'],
				dtnascimento = teste[x]['dtnascimento'],
				curso = Curso.objects.get(pk = teste[x]['curso']),
				periodo = teste[x]['periodo'],
				telefone = teste[x]['telefone'],
				email = teste[x]['email'],
				usuario = User.objects.get(pk = 1))
			aluno.save()
		return HttpResponseRedirect("/lista/"+str(objeto))
	if str(objeto) == 'empresa':
		arquivo = file('/opt/tpcavancados/jsonempresa')
		teste = json.load(arquivo)
		for x in range(len(teste)):
			empresa = Empresa(
				nome = teste[x]['nome'],
				contato = teste[x]['contato'],
				telefone = teste[x]['telefone'],
				email = teste[x]['email'],
				site = teste[x]['site'],
				logradouro = teste[x]['logradouro'],
				nrimovel = teste[x]['nrimovel'],
				complemento = teste[x]['complemento'],
				cidade = teste[x]['cidade'],
				uf = teste[x]['uf'],
				cep = teste[x]['cep'],
				usuario = User.objects.get(pk = 1))
			empresa.save()
		return HttpResponseRedirect("/lista/"+str(objeto))
		






















		








