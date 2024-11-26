from rest_framework import viewsets, generics
from plataformav.models import Account, Post, PostFeed, Comment
from plataformav.serializers import AccountSerializer, PostSerializer, PostFeedSerializer, CommentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from plataformav.pagination import FeedPagination
from .models import create_user_for_account

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all().order_by("id")
    serializer_class = AccountSerializer

    def perform_create(self, serializer):
        account = serializer.save()
        create_user_for_account(account) 

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