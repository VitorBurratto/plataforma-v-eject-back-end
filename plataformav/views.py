from plataformav.models import Account, Post
from plataformav.serializers import AccountSerializer, PostSerializer
from rest_framework import viewsets

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer