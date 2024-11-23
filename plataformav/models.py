from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    description = models.CharField(max_length=100, blank=False, verbose_name='Descrição')
    image = models.CharField(max_length=5, choices=IMAGEPOST, blank=False, null=False, default='I')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, related_name='posts')
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.code

class PostFeed(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.account

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(verbose_name='Conteúdo do Comentário')
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.account.name} no Post {self.post.code}"

# Sinal para criar um PostFeed automaticamente quando um novo Post é criado
@receiver(post_save, sender=Post)
def createPostFeed(sender, instance, created, **kwargs):
    if created:
        # Cria um PostFeed somente para a conta do autor do post
        if instance.account:
            PostFeed.objects.create(account=instance.account, post=instance)