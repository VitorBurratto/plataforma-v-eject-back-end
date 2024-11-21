from django.contrib import admin
from django.urls import path,include
from plataformav.views import AccountViewSet, PostViewSet, PostFeedViewSet, CommentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('accounts', AccountViewSet, basename = 'Accounts')
router.register('posts', PostViewSet, basename = 'Posts')
router.register('postfeeds', PostFeedViewSet, basename = 'PostFeed')
router.register('comments', CommentViewSet, basename = 'Comments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]