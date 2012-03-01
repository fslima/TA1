# -* coding:utf-8 -*-

from django import forms
from django.forms.extras.widgets import SelectDateWidget
from models import Aluno, Curso, Empresa, Oportunidade, Encaminhamento, Evento
from django.core.exceptions import ValidationError

class FormAluno(forms.ModelForm):
	dtnascimento = forms.DateField(
				label = 'Data de Nascimento',
				widget = forms.DateInput(format = '%d/%m/%Y'),
				input_formats = ['%d/%m/%Y'],
			)
	periodo = forms.ChoiceField([('1','1'), ('2','2'), ('3','3'),('4','4'), 
				     ('5','5'),('6','6'), ('7','7'), ('8','8')], 
				     initial = ('1','1'))
	telefone = forms.CharField(min_length = 10, max_length = 10)

	class Meta:
		model = Aluno
		fields = ('matricula', 'nome', 'dtnascimento', 'curso', 'periodo', 'email', 'telefone')

class FormFiltraAluno(forms.Form):
	todos_cursos = Curso.objects.all().order_by('nome')
	opcoes = [(0,'')]
	for i in todos_cursos:
		opcoes.append((i.id, i.nome))
	matricula = forms.CharField(required = False)
	nome = forms.CharField(required = False)
	curso = forms.ChoiceField(opcoes, required = False)	

	fields = ('matricula','nome', 'curso')

class FormCurso(forms.ModelForm):
	tpcurso = forms.ChoiceField(
			[('',''), ('Básico','Básico'), ('Técnico','Técnico'),
			('Graduação','Graduação'), ('Pós-Graduação','Pós-Graduação')], 
			initial = ('',''), label = 'Tipo do Curso')
	nome = forms.CharField(label = 'Curso')
	nrperiodos = forms.CharField(label = 'Nº de Períodos')

	class Meta:
		model = Curso
		fields = ('tpcurso', 'nome', 'nrperiodos')

class FormFiltraCurso(forms.Form):
	tpcurso = forms.ChoiceField(
			[('',''), ('Básico','Básico'), ('Técnico','Técnico'),
			('Graduação','Graduação'), ('Pós-Graduação','Pós-Graduação')], 
			initial = ('',''), label = 'Tipo do Curso',
			required = False)
	nome = forms.CharField(label = 'Curso', required = False)
	fields = ('tpcurso', 'nome', )

class FormEmpresa(forms.ModelForm):
	nome = forms.CharField(label = 'Empresa')
	contato = forms.CharField(label = 'Pessoa de Contato')
	telefone = forms.CharField(min_length = 10, max_length = 10)
	nrimovel = forms.IntegerField(label = 'Nº')
	complemento = forms.CharField(max_length = 50, required = False)
	uf = forms.ChoiceField([('',''), ('AC','AC'), ('AL','AL'), ('AM','AM'),
				('AP','AP'),('BA','BA'), ('CE','CE'), ('DF','DF'),
				('ES','ES'),('GO','GO'), ('MA','MA'), ('MG','MG'),
				('MS','MS'),('MT','MT'), ('PA','PA'), ('PB','PB'),
				('PI','PI'),('PI','PI'), ('PR','PR'), ('RJ','RJ'),
				('RN','RN'),('RO','RO'), ('RR','RR'), ('RS','RS'),
				('SC','SC'),('SE','SE'),('SP','SP'), ('TO','TO')], 
				initial = ('',''),
				label = 'Estado')
	cep = forms.CharField(min_length = 8, max_length = 8)

	class Meta:
		model = Empresa
		fields = ('nome', 'contato', 'telefone', 'email', 'site', 'logradouro', 'nrimovel', 'complemento', 'bairro', 'cidade', 'uf', 'cep')

class FormFiltraEmpresa(forms.Form):
	nome = forms.CharField(label = 'Empresa', required = False)
	bairro = forms.CharField(required = False)
	cidade = forms.CharField(required = False)
	uf = forms.ChoiceField([('',''), ('AC','AC'), ('AL','AL'), ('AM','AM'),
				('AP','AP'),('BA','BA'), ('CE','CE'), ('DF','DF'),
				('ES','ES'),('GO','GO'), ('MA','MA'), ('MG','MG'),
				('MS','MS'),('MT','MT'), ('PA','PA'), ('PB','PB'),
				('PI','PI'),('PI','PI'), ('PR','PR'), ('RJ','RJ'),
				('RN','RN'),('RO','RO'), ('RR','RR'), ('RS','RS'),
				('SC','SC'),('SE','SE'),('SP','SP'), ('TO','TO')], 
				initial = ('',''),
				label = 'Estado', required = False)
	fields = ('nome', 'bairro', 'cidade', 'uf')

class FormOportunidade(forms.ModelForm):
	tpoportunidade = forms.ChoiceField(
			[('',''), ('Bolsa','Bolsa'), ('Estágio','Estágio'),('Emprego','Emprego')], 
			initial = ('',''), label = 'Tipo da Oportunidade')
	
	dtinicio = forms.DateField(
				label = 'Abertura das Inscrições',
				widget = forms.DateInput(format = '%d/%m/%Y'),
				input_formats = ['%d/%m/%Y'])
	dtfim = forms.DateField(
				label = 'Término das Inscrições',
				widget = forms.DateInput(format = '%d/%m/%Y'),
				input_formats = ['%d/%m/%Y'])
	nrvagas = forms.CharField(label = 'Nº de Vagas')
	descoportunidade = forms.CharField(
				label = 'Descrição',
				widget = forms.Textarea()
			)

	class Meta:
		model = Oportunidade
		fields = ('id', 'vaga', 'tpoportunidade', 'empresa', 'dtinicio', 'dtfim', 'nrvagas', 'descoportunidade')

class FormCursoOportunidade(forms.ModelForm):

	class Meta:
		model = Oportunidade
		fields = ('vaga', 'curso')

class FormFiltraOportunidade(forms.Form):
	todas_empresas = Empresa.objects.all().order_by('nome')
	opcoes = [(0,'')]
	for i in todas_empresas:
		opcoes.append((i.id, i.nome))
	tpoportunidade = forms.ChoiceField(
			[('',''), ('Bolsa','Bolsa'), ('Estágio','Estágio'),('Emprego','Emprego')], 
			initial = ('',''), label = 'Tipo da Oportunidade', required = False)
	empresa = forms.ChoiceField(opcoes)
	todos_cursos = Curso.objects.all().order_by('nome')
	opcoes = [(0,'')]
	for i in todos_cursos:
		opcoes.append((i.id, i.nome))
	curso = forms.ChoiceField(opcoes, required = False)
	fields = ('tpoportunidade','empresa','curso')
	
class FormEncaminhamento(forms.ModelForm):
	dtinicio = forms.DateField(
				label = 'Início do Contrato',
				widget = forms.DateInput(format = '%d/%m/%Y'),
				input_formats = ['%d/%m/%Y'])
	dtfim = forms.DateField(
				label = 'Final do Contrato',
				widget = forms.DateInput(format = '%d/%m/%Y'),
				input_formats = ['%d/%m/%Y'])
	situacao = forms.ChoiceField(
			[('Em Andamento','Em Andamento'), ('Pendente Relatório Final','Pendente Relatório Final'), 
			('Concluído','Concluído')], initial = ('Em Andamento','Em Andamento'), label = 'Situação')

	class Meta:
		model = Encaminhamento
		fields = ('oportunidade', 'aluno', 'dtinicio', 'dtfim', 'situacao')

class FormFiltraEncaminhamento(forms.Form):
	todas_empresas = Empresa.objects.all().order_by('nome')
	todos_alunos = Aluno.objects.all().order_by('nome')
	tpoportunidade = forms.ChoiceField(
			[('',''), ('Bolsa','Bolsa'), ('Estágio','Estágio'),('Emprego','Emprego')], 
			initial = ('',''), label = 'Tipo da Oportunidade', required = False)
	opcoes = [(0,'')]
	for i in todas_empresas:
		opcoes.append((i.id, i.nome))
	empresa = forms.ChoiceField(opcoes)
	opcoes = [(0,'')]
	for i in todos_alunos:
		opcoes.append((i.id, i.nome))
	aluno = forms.ChoiceField(opcoes, required = False)
	situacao = forms.ChoiceField(
			[('',''),('Em Andamento','Em Andamento'), ('Pendente Relatório Final','Pendente Relatório Final'), 
			('Concluído','Concluído')], initial = ('',''), label = 'Situação', required = False)
	fields = ('empresa','tpoportunidade','aluno','situacao')


class FormEvento(forms.ModelForm):
	nome = forms.CharField(label = 'Evento')
	nrvagas = forms.CharField(label = 'Nº de Vagas')
	dtinicio = forms.DateField(
				label = 'Início do Evento',
				widget = forms.DateInput(format = '%d/%m/%Y'),
				input_formats = ['%d/%m/%Y'])
	dtfim = forms.DateField(
				label = 'Final do Evento',
				widget = forms.DateInput(format = '%d/%m/%Y'),
				input_formats = ['%d/%m/%Y'])
	descevento = forms.CharField(
				label = 'Informações sobre o Evento',
				widget = forms.Textarea()
			)

	class Meta:
		model = Evento
		fields = ('nome', 'nrvagas', 'dtinicio', 'dtfim', 'descevento')

class FormParticipante(forms.ModelForm):

	class Meta:
		model = Evento
		fields = ('nome', 'participante')

class FormFiltraEvento(forms.Form):
	nome = forms.CharField(label = 'Evento', required = False)
	todos_alunos = Aluno.objects.all().order_by('nome')
	opcoes = [(0,'')]
	for i in todos_alunos:
		opcoes.append((i.id, i.nome))
	participante = forms.ChoiceField(opcoes, required = False)
	fields = ('nome','participante')


















