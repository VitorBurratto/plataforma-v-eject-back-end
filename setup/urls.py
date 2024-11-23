from django.contrib import admin
from django.urls import path, include

from plataformav.views import (AccountViewSet,PostViewSet,PostFeedViewSet,ListPostFeedView, CommentViewSet)
from rest_framework import routers

#from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register('accounts', AccountViewSet, basename='Accounts')
router.register('posts', PostViewSet, basename='Posts')
router.register('postfeeds', PostFeedViewSet, basename='PostFeed')
router.register('comments', CommentViewSet, basename='Comments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('accounts/<int:pk>/postfeeds/', ListPostFeedView.as_view()),
    #path('token/', TokenObtainPairView.as_view()),
    #path('token/refresh/', TokenRefreshView.as_view()),
]   