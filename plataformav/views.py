from rest_framework import viewsets, generics
from plataformav.models import Account, Post, PostFeed, Comment, Like
from plataformav.serializers import AccountSerializer, PostSerializer, PostFeedSerializer, CommentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from plataformav.pagination import FeedPagination
from .permissions import IsAccountOwner
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated, IsAccountOwner]  # Garantir que o usuário esteja autenticado

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("id")
    serializer_class = PostSerializer

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):
        try:
            post = self.get_object()  # Obtém o post com base no ID
        except Post.DoesNotExist:
            raise NotFound(detail="Post not found.")  # Caso o post não exista, retorna erro 404

        user = request.user
        
        # Verifica se o usuário já curtiu o post
        existing_like = Like.objects.filter(user=user, post=post).first()
        
        if existing_like:  # Se já existe uma curtida, descurtir
            existing_like.delete()  # Remove o like
            post.likes -= 1  # Decrementa o número de curtidas
            action = 'descurtido'
        else:  # Se não existe uma curtida, curtir
            Like.objects.create(user=user, post=post)  # Cria uma nova curtida
            post.likes += 1  # Incrementa o número de curtidas
            action = 'curtido'

        post.save()  # Salva as alterações no post

        return Response({'status': f'Post {action}', 'likes': post.likes})

class PostFeedViewSet(viewsets.ModelViewSet):
    queryset = PostFeed.objects.all().order_by("id")
    serializer_class = PostFeedSerializer
    pagination_class = FeedPagination  # Paginação personalizada

class ListPostFeedView(generics.ListAPIView):
    serializer_class = PostFeedSerializer

    def get_queryset(self):
        """
        Descrição de View
        - Lista Post po id de ListPost
        Parâmetros:
        - pk (int): O indentificador promário do objeto. Deve ser um Número inteiro.
        """
        return PostFeed.objects.filter(account_id=self.kwargs['pk'])

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("id")
    serializer_class = CommentSerializer

    @action(detail=False, methods=["get"], url_path=r'post/(?P<post_id>[^/.]+)')
    def get_comments_by_post(self, request, post_id=None):
        comments = Comment.objects.filter(post_id=post_id)
        
        # Adicionar paginação se necessário
        page = self.paginate_queryset(comments)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(comments, many=True)
        return Response(serializer.data)
