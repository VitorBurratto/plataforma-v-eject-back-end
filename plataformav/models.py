from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome de Usuário')
    email = models.EmailField(blank=False, max_length=40, verbose_name='Email do Usuário')
    cpf = models.CharField(max_length=11, verbose_name='CPF do Usuário')
    dateBirth = models.DateTimeField(verbose_name='Data de Nascimento do Usuário')
    cellphone = models.CharField(max_length=14, verbose_name='Celular do Usuário')

    def __str__(self):
        return self.name


class Post(models.Model):
    IMAGEPOST = (
        ('I', 'Somente Imagem'),
        ('I+D', 'Imagem e Descrição'),
        ('I+D+C', 'Imagem, Descrição e Comentários'),
    )
    
    code = models.CharField(max_length=10, verbose_name='Código')
    description = models.CharField(max_length=100, blank=False, verbose_name='Descrição')  # Corrigido aqui
    image = models.CharField(max_length=5, choices=IMAGEPOST, blank=False, null=False, default='I')

    def __str__(self):
        return self.code