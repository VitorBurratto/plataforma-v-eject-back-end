from django.test import TestCase
from plataformav.models import Account, Post, PostFeed, Comment
from plataformav.serializers import AccountSerializer, PostSerializer, PostFeedSerializer, CommentSerializer
from django.contrib.auth.models import User

class SerializerAccountTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='user_example', password='password123')

        self.account = Account(
            username='TesteUserName',
            name='Teste de Conta',
            password='senha123',
            email='teste@gmail.com',
            cpf='12345678901',
            cellphone='(84) 99999-9999'
        )
        self.serializer = AccountSerializer(instance=self.account)
    
    def test_verifica_campos_serializados_de_account(self):
        dados = self.serializer.data
        self.assertEqual(
            set(dados.keys()),
            set(['id', 'password', 'name', 'email', 'cpf', 'cellphone', 'username', 'user'])
        )

class SerializerPostTestCase(TestCase):
    def setUp(self):
        self.account = Account.objects.create(
            username='TesteUserName',
            name='Teste de Conta',
            password='senha123',
            email='teste@gmail.com',
            cpf='12345678901',
            cellphone='(84) 99999-9999'
        )
        self.post = Post.objects.create(
            description='Descrição de teste',
            account=self.account
        )
        self.serializer = PostSerializer(instance=self.post)

    def test_verifica_campos_serializados_de_post(self):
        dados = self.serializer.data
        self.assertEqual(
            set(dados.keys()),
            set(['id', 'description', 'account', 'postType', 'image', 'code', 'likes', 'comments'])
        )
        self.assertEqual(dados['description'], self.post.description)
        self.assertEqual(dados['account'], self.post.account.id)

class SerializerPostFeedTestCase(TestCase):
    def setUp(self):
        self.account = Account.objects.create(
            username='TesteUserName',
            name='Teste de Conta',
            password='senha123',
            email='teste@gmail.com',
            cpf='12345678901',
            cellphone='(84) 99999-9999'
        )
        self.post = Post.objects.create(
            description='Descrição de teste',
            account=self.account
        )
        self.post_feed = PostFeed.objects.create(account=self.account, post=self.post)
        self.serializer = PostFeedSerializer(instance=self.post_feed)

    def test_verifica_campos_serializados_de_post_feed(self):
        dados = self.serializer.data
        self.assertEqual(
            set(dados.keys()),
            set(['id', 'account', 'post'])
        )
        self.assertEqual(dados['account'], self.post_feed.account.id)
        self.assertEqual(dados['post'], self.post_feed.post.id)

    def test_verifica_id_do_post_feed(self):
        dados = self.serializer.data
        self.assertIsInstance(dados['id'], int)

class SerializerCommentTestCase(TestCase):
    def setUp(self):
        self.account = Account.objects.create(
            username='TesteUserName',
            name='Teste de Conta',
            password='senha123',
            email='teste@gmail.com',
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
        self.serializer = CommentSerializer(instance=self.comment)

    def test_verifica_campos_serializados_de_comment(self):
        dados = self.serializer.data
        self.assertEqual(
            set(dados.keys()),
            set(['id', 'post', 'account', 'content', 'createdAt'])
        )