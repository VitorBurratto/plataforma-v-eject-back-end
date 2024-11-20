from django.contrib import admin
from django.urls import path,include
from plataformav.views import AccountViewSet, PostViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('accounts',AccountViewSet,basename='Accounts')
router.register('posts', PostViewSet,basename='Post')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
