from rest_framework.permissions import IsAuthenticated 
from rest_framework import viewsets, generics
from plataformav.models import Account, Post, PostFeed, Comment
from plataformav.serializers import AccountSerializer, PostSerializer, PostFeedSerializer, CommentSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated,] 

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer 
    permission_classes = [IsAuthenticated,]

class PostFeedViewSet(viewsets.ModelViewSet):
    queryset = PostFeed.objects.all()
    serializer_class = PostFeedSerializer
    permission_classes = [IsAuthenticated,]

class ListPostFeedView(generics.ListAPIView):
    serializer_class = PostFeedSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return PostFeed.objects.filter(account_id=self.kwargs['pk'])

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated,]