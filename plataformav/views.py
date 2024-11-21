from plataformav.models import Account, Post, PostFeed, Comment
from plataformav.serializers import AccountSerializer, PostSerializer, PostFeedSerializer, CommentSerializer
from rest_framework import viewsets

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class PostFeedViewSet(viewsets.ModelViewSet):
    queryset = PostFeed.objects.all()
    serializer_class = PostFeedSerializer



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer