from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import random
import string
from django.utils import timezone

# Modelo que representa a conta do usuário no sistema
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, editable=False) # Relacionamento com o modelo User
    username = models.CharField(max_length=150, verbose_name='Nome de Usuário Admin', blank=True, null=True) # Nome de usuário
    name = models.CharField(max_length=100, verbose_name='Nome do Perfil') # Nome do perfil do usuário
    password = models.CharField(max_length=128, verbose_name='Senha', blank=False)
    email = models.EmailField(blank=False, max_length=40, verbose_name='Email do Usuário')
    cpf = models.CharField(max_length=11, verbose_name='CPF do Usuário')
    cellphone = models.CharField(max_length=14, verbose_name='Celular do Usuário')

    def __str__(self):
        return self.adminUsername if self.adminUsername else f"Account {self.id}"

def create_user_for_account(account): # Função para criar um usuário no modelo User a partir do Account
    username = account.email.split('@')[0]
    if User.objects.filter(username=username).exists():  # Verifica se o nome de usuário já existe
        username = f"{username}_{random.randint(1000, 9999)}" # Gera um nome único

    user = User.objects.create_user(
        username=username, # Cria o usuário com o nome de usuário gerado
        email=account.email # Email do usuário
    )
    user.set_password(account.password) # Criptografa a senha do usuário
    user.save()

    account.user = user # Associa o usuário ao modelo Account
    account.save()
    
# Modelo que representa os posts criados pelos usuários
class Post(models.Model):
    # Opções disponíveis para o tipo de post
    postTypeChoices = (
        ('I', 'Somente Imagem'),
        ('I+C', 'Imagem e Comentários'),
        ('I+D', 'Imagem e Descrição'),
        ('D+C', 'Descrição e Comentários'),
        ('I+D+C', 'Imagem, Descrição e Comentários'),
    )

    code = models.CharField(max_length=10, verbose_name='Código', blank=True, editable=False) # Código único para identificar o post
    description = models.CharField(max_length=100, blank=True, verbose_name='Descrição') # Descrição opcional
    image = models.ImageField(upload_to='post_images/', verbose_name='Imagem', blank=True)
    postType = models.CharField(max_length=5, choices=postTypeChoices, default='I', verbose_name='Tipo de Post') # Tipo do post com base nas opções definidas
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, related_name='posts')  # Conta que criou o post
    likes = models.PositiveIntegerField(default=0, editable=False)
    comments = models.TextField(verbose_name='Comentários', blank=True, editable=False) 

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        if not self.code:  # Se o código não estiver definido
            self.code = ''.join(random.choices(string.ascii_letters + string.digits, k=10))  # Gera um código único
        super().save(*args, **kwargs)

# Modelo para armazenar as curtidas (likes) em posts
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relaciona o like ao usuário
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # Relaciona o like ao post

    class Meta:
        unique_together = ('user', 'post')  # Garante que um usuário só possa curtir um post uma vez

    def __str__(self):
        return f"Like de {self.user.username} no post {self.post.code}"

# Modelo que representa o feed de posts
class PostFeed(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, editable=False)  # Relacionamento com a conta
    post = models.ForeignKey(Post, on_delete=models.CASCADE, editable=False)  # Relacionamento com o post

    def __str__(self):
        return str(self.account)

# Modelo para armazenar comentários em posts
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')  # Relacionamento com o post
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='comments')  # Relacionamento com a conta
    content = models.TextField(verbose_name='Conteúdo do Comentário')
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.account.name} no Post {self.post.code}"

# Sinal que cria automaticamente um PostFeed
@receiver(post_save, sender=Post)
def createPostFeed(sender, instance, created, **kwargs):
    if created:
        if instance.account:  # Certifica-se de que há uma conta associada ao post
            PostFeed.objects.create(account=instance.account, post=instance)