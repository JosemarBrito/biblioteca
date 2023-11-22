from django.db import models
from datetime import date
class Livros (models.Model):
    nome = models.CharField (max_length=50)
    autor = models.CharField(max_length=50, blank = True)
    tema = models.CharField(max_length=50, blank = True)
    data_cadastro = models.DateField(default = date.today)
    emprestado = models.BooleanField(default=False)
    nome_emprestado = models.CharField(max_length=50, blank = True)
    data_emprestimo = models.DateTimeField(blank = True)
    data_devolucao = models.DateTimeField(blank = True)
    tempo_duracao = models.DateField(blank = True)

    
    class Meta:
        verbose_name = 'Livro'
        