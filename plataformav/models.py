from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
import random
import string
from django.utils import timezone

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, editable=False)
    adminUsername = models.CharField(max_length=150, verbose_name='Nome de Usuário Admin', blank=True, null=True)
    password = models.CharField(max_length=128, verbose_name='Senha do Superusuário', blank=False)
    name = models.CharField(max_length=100, verbose_name='Nome do Perfil do Usuário')
    email = models.EmailField(blank=False, max_length=40, verbose_name='Email do Usuário')
    cpf = models.CharField(max_length=11, verbose_name='CPF do Usuário')
    dateBirth = models.DateTimeField(verbose_name='Data de Nascimento do Usuário', default=timezone.now)
    cellphone = models.CharField(max_length=14, verbose_name='Celular do Usuário')

    def __str__(self):
        return self.adminUsername if self.adminUsername else f"Account {self.id}"

def create_user_for_account(account):
    group_name = 'Commons Users'
    group, created = Group.objects.get_or_create(name=group_name)

    username = account.email
    if User.objects.filter(username=username).exists():
        username = f"{account.email.split('@')[0]}_{random.randint(1000, 9999)}" 
    user = User.objects.create_user(
        username=username, 
        password=account.password,
        email=account.email  
    )

    account.user = user
    account.save()

    user.groups.add(group)
    user.save()

class Post(models.Model):
    postTypeChoices = (
        ('I', 'Somente Imagem'),
        ('I+C', 'Imagem e Comentários'),
        ('I+D', 'Imagem e Descrição'),
        ('D+C', 'Descrição e Comentários'),
        ('I+D+C', 'Imagem, Descrição e Comentários'),
    )
    
    code = models.CharField(max_length=10, verbose_name='Código', blank=True, editable=False)
    description = models.CharField(max_length=100, blank=True, verbose_name='Descrição')
    image = models.ImageField(upload_to='post_images/', verbose_name='Imagem', blank=True)
    postType = models.CharField(max_length=5, choices=postTypeChoices, default='I', verbose_name='Tipo de Post')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, related_name='posts')
    likes = models.PositiveIntegerField(default=0, editable=False)
    comments = models.TextField(verbose_name='Comentários', blank=True, editable=False)

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        super().save(*args, **kwargs)

class PostFeed(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, editable=False)

    def __str__(self):
        return str(self.account)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(verbose_name='Conteúdo do Comentário')
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.account.name} no Post {self.post.code}"

# Signal to create PostFeed when a Post is created
@receiver(post_save, sender=Post)
def createPostFeed(sender, instance, created, **kwargs):
    if created:
        if instance.account:
            PostFeed.objects.create(account=instance.account, post=instance)