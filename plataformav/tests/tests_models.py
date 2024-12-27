from django.test import TestCase
from django.contrib.auth.models import User
from plataformav.models import Account, Post, Like, PostFeed, Comment

class ModelAccountTestCase(TestCase):
    def setUp(self):
        self.account = Account.objects.create(
            adminUsername='TesteAdmin',
            password='senha123',
            name='Teste de Conta',
            email='teste@gmail.com',
            cpf='12345678901',
            cellphone='(84) 99999-9999'
        )

    def test_verifica_atributos_de_account(self):
        self.assertEqual(self.account.adminUsername, 'TesteAdmin')
        self.assertEqual(self.account.name, 'Teste de Conta')
        self.assertEqual(self.account.email, 'teste@gmail.com')
        self.assertEqual(self.account.cpf,'12345678901')
        self.assertEqual(self.account.cellphone, '(84) 99999-9999')

class ModelPostTestCase(TestCase):
    def setUp(self):
        self.account = Account.objects.create(
            adminUsername='TesteAdmin',
            password='senha123',
            name='Teste de Conta',
            email='teste@teste.com',
            cpf='12345678901',
            cellphone='(84) 99999-9999'
        )
        self.post = Post.objects.create(
            description='Descrição de teste',
            account=self.account
        )

    def test_verifica_atributos_de_post(self):
        self.assertEqual(self.post.description, 'Descrição de teste')
        self.assertEqual(self.post.account, self.account)

class ModelLikeTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='usuario_teste',
            password='senha123'
        )
        self.account = Account.objects.create(
            adminUsername='TesteAdmin',
            password='senha123',
            name='Teste de Conta',
            email='teste@teste.com',
            cpf='12345678901',
            cellphone='(84) 99999-9999'
        )
        self.post = Post.objects.create(
            description='Descrição de teste',
            account=self.account
        )
        self.like = Like.objects.create(user=self.user, post=self.post)

    def test_verifica_atributos_de_like(self):
        self.assertEqual(self.like.user, self.user)
        self.assertEqual(self.like.post, self.post)

class ModelPostFeedTestCase(TestCase):
    def setUp(self):
        self.account = Account.objects.create(
            adminUsername='TesteAdmin',
            password='senha123',
            name='Teste de Conta',
            email='teste@teste.com',
            cpf='12345678901',
            cellphone='(84) 99999-9999'
        )
        self.post = Post.objects.create(
            description='Descrição de teste',
            account=self.account
        )
        self.post_feed = PostFeed.objects.create(account=self.account, post=self.post)

    def test_verifica_atributos_de_post_feed(self):
        self.assertEqual(self.post_feed.account, self.account)
        self.assertEqual(self.post_feed.post, self.post)

class ModelCommentTestCase(TestCase):
    def setUp(self):
        self.account = Account.objects.create(
            adminUsername='TesteAdmin',
            password='senha123',
            name='Teste de Conta',
            email='teste@teste.com',
            cpf='12345678901',
            cellphone='(84) 99999-9999'
        )
        self.post = Post.objects.create(
            description='Descrição de teste',
            account=self.account
        )
        self.comment = Comment.objects.create(
            post=self.post,
            account=self.account,
            content='Comentário de teste'
        )

    def test_verifica_atributos_de_comment(self):
        self.assertEqual(self.comment.post, self.post)
        self.assertEqual(self.comment.account, self.account)
        self.assertEqual(self.comment.content, 'Comentário de teste')