# -*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

class Curso(models.Model):
	def __unicode__(self):
		return self.nome

	tpcurso = models.CharField(max_length = 50)
	nome = models.CharField(max_length = 50)
	nrperiodos = models.IntegerField()

	def validaAtrib(self):
		return 'validos'

	class Meta:
		db_table = 'curso'

class Aluno(models.Model):
	def __unicode__(self):
		return self.nome

	matricula = models.CharField(max_length = 50, unique = True)
	nome = models.CharField(max_length = 50)
	dtnascimento = models.DateField()
	curso = models.ForeignKey(Curso, related_name = 'curso_do_aluno')
	periodo = models.IntegerField()	
	telefone = models.BigIntegerField(max_length = 10)
	email = models.EmailField(max_length = 50)
	usuario = models.ForeignKey(User)

	def validaAtrib(self):
		return 'validos'
	
	class Meta:
		db_table = 'aluno'

class Empresa(models.Model):
	def __unicode__(self):
		return self.nome

	nome = models.CharField(max_length = 30)
	contato = models.CharField(max_length = 50)
	telefone = models.BigIntegerField(max_length = 10)
	email = models.EmailField(max_length = 50)
	site = models.URLField()
	logradouro = models.CharField(max_length = 50)
	nrimovel = models.IntegerField()
	complemento = models.CharField(max_length = 50)
	bairro = models.CharField(max_length = 50)
	cidade = models.CharField(max_length = 50)
	uf = models.CharField(max_length = 2)
	cep = models.BigIntegerField(max_length = 8)
	usuario = models.ForeignKey(User)

	def validaAtrib(self):
		return 'validos'

	class Meta:
		db_table = 'empresa'

class Oportunidade(models.Model):
	def __unicode__(self):
		return self.vaga

	vaga = models.CharField(max_length = 50)
	tpoportunidade = models.CharField(max_length = 50)
	empresa = models.ForeignKey(Empresa, related_name = 'empresa_da_oportunidade')
	curso = models.ManyToManyField(Curso, related_name = 'curso_da_oportunidade')
	descoportunidade = models.TextField(max_length = 100)
	dtinicio = models.DateField()
	dtfim = models.DateField()
	nrvagas = models.IntegerField()
	usuario = models.ForeignKey(User)

	def validaAtrib(self):
		if self.dtfim < self.dtinicio:
			return 'A Data de Término das Inscrições não pode ser inferior a de Abertura'
		else:
			return 'validos'

	class Meta:
		db_table = 'oportunidade'

class Evento(models.Model):
	def __unicode__(self):
		return self.nome

	nome = models.CharField(max_length = 50)
	descevento = models.TextField(max_length = 100)
	nrvagas = models.IntegerField()
	dtinicio = models.DateField()
	dtfim = models.DateField()
	participante = models.ManyToManyField(Aluno, related_name = 'participante_do_evento')
	usuario = models.ForeignKey(User)

	def validaAtrib(self):
		if self.dtfim < self.dtinicio:
			return 'A Data Final do Contrato não pode inferior a do Início'
		else:
			return 'validos'

	class Meta:
		db_table = 'evento'

class Encaminhamento(models.Model):
	def __unicode__(self):
		return self.aluno.nome

	oportunidade = models.ForeignKey(Oportunidade, related_name = 'oportunidade_do_encaminhamento')
	aluno = models.ForeignKey(Aluno, related_name = 'aluno_do_encaminhamento', unique = True)
	dtinicio = models.DateField()
	dtfim = models.DateField()
	dtpublicacao = models.DateField(auto_now_add = True)
	situacao = models.CharField(max_length = 50)
	usuario = models.ForeignKey(User)

	def validaAtrib(self):
		if self.dtfim < self.dtinicio:
			return 'A Data Final do Contrato não pode ser inferior a do Início'
		if self.dtfim - self.dtinicio > timedelta(366):
			return 'O Período máximo do contrato não pode ser superior a 1 Ano'
		if self.dtfim - self.dtinicio < timedelta(180):
			return 'O Período mínimo do contrato não pode ser inferior a 6 meses'
		if self.oportunidade.tpoportunidade == 'Emprego':
			return 'Não são cadastrados Encaminhamentos para Emprego, apenas para Bolsa e Estágio'
		return 'validos'

	class Meta:
		db_table = 'encaminhamento'
