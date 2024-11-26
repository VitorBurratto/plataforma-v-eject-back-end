from rest_framework import viewsets, generics
from plataformav.models import Account, Post, PostFeed, Comment
from plataformav.serializers import AccountSerializer, PostSerializer, PostFeedSerializer, CommentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from plataformav.pagination import FeedPagination
from rest_framework import viewsets
from .permissions import IsAccountOwner

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAccountOwner]

    def get_queryset(self):
        # Retorna a conta do usuário logado com base no ID passado na URL
        return Account.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Quando a conta é criada, associamos ao usuário logado
        serializer.save(user=self.request.user)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("id")
    serializer_class = PostSerializer
    
    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        post.likes += 1
        post.save()
        
        return Response({'status': 'post liked', 'likes': post.likes})

class PostFeedViewSet(viewsets.ModelViewSet):
    queryset = PostFeed.objects.all().order_by("id")
    serializer_class = PostFeedSerializer

class ListPostFeedView(generics.ListAPIView):
    serializer_class = PostFeedSerializer

    def get_queryset(self):
        return PostFeed.objects.filter(account_id=self.kwargs['pk'])

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("id")
    serializer_class = CommentSerializer

class PostFeedViewSet(viewsets.ModelViewSet):
    queryset = PostFeed.objects.all().order_by("id")
    serializer_class = PostFeedSerializer
    pagination_class = FeedPagination