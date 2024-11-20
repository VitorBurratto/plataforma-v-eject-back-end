from django.contrib import admin
from plataformav.models import Account, Post


class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'cpf', 'dateBirth', 'cellphone')
    list_display_links = ('id', 'name')
    list_per_page = 20
    search_fields = ('name',)  # Corrigido: Agora é uma tupla


admin.site.register(Account, AccountAdmin)  # Corrigido: A classe foi renomeada para AccountAdmin


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'description')
    list_display_links = ('id', 'code')
    search_fields = ('code',)  # Corrigido: Agora é uma tupla


admin.site.register(Post, PostAdmin)  # Corrigido: A classe foi renomeada para PostAdmin