from django.contrib import admin
from django.urls import path, include

from plataformav.views import (AccountViewSet,PostViewSet,PostFeedViewSet,ListPostFeedView, CommentViewSet)
from rest_framework import routers

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Documentação da API",
      default_version='v1',
      description="Documentação mini X (Plataforma V)",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

router = routers.DefaultRouter()
router.register('accounts', AccountViewSet, basename='Accounts')
router.register('posts', PostViewSet, basename='Posts')
router.register('postfeeds', PostFeedViewSet, basename='PostFeed')
router.register('comments', CommentViewSet, basename='Comments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('accounts/<int:pk>/postfeeds/', ListPostFeedView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]   