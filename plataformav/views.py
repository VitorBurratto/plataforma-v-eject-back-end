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
            post.likes -= 1 
            action = 'descurtido'
        else:  # Se não existe uma curtida, curtir
            Like.objects.create(user=user, post=post)  # Cria uma nova curtida
            post.likes += 1  
            action = 'curtido'

        post.save()  # Salva as alterações no post

        return Response({'status': f'Post {action}', 'likes': post.likes})

class PostFeedViewSet(viewsets.ModelViewSet):
    queryset = PostFeed.objects.all().order_by("id")
    serializer_class = PostFeedSerializer
    pagination_class = FeedPagination

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

    # Definir uma ação POST para criar comentário
    @action(detail=False, methods=["post"], url_path=r'createComment/(?P<post_id>[^/.]+)')
    def createComment(self, request, post_id=None):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({"detail": "Post not found."})
        
        # Cria o novo comentário associado ao post
        content = request.data.get("content")
        if not content:
            return Response({"detail": "Conteúdo do comentário não fornecido."})
        
        comment = Comment.objects.create(
            content=content,
            post=post,
            account=request.user.account  # Assumindo que você tem um relacionamento com a conta
        )
        
        serializer = self.get_serializer(comment)
        return Response(serializer.data)