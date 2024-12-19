from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
from plataformav.models import Account, Post, PostFeed, Comment

class AccountAdmin(admin.ModelAdmin):
#faz com que o Account só tenha acesso ao seu próprio Id e não posso modificar os dos outros
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Limita os resultados no Admin para o usuário logado
        return qs.filter(user=request.user)

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user:
            return False  # Não permite editar outro account
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user:
            return False  # Não permite deletar outro account
        return super().has_delete_permission(request, obj)

admin.site.register(Account, AccountAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'description', 'account')
    list_display_links = ('id', 'code')
    search_fields = ('code',)

admin.site.register(Post, PostAdmin)

class PostFeedAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'post')

admin.site.register(PostFeed, PostFeedAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'post', 'content', 'createdAt')
    search_fields = ('content',)
    list_filter = ('createdAt',)

admin.site.register(Comment, CommentAdmin)

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['get_admin_username', 'email', 'first_name', 'last_name', 'is_staff']
    list_filter = ['is_staff', 'is_active']
    search_fields = ['username', 'email']

    def get_admin_username(self, obj):
        return obj.account.adminUsername if hasattr(obj, 'account') else None
    
    get_admin_username.admin_order_field = 'account__adminUsername'
    get_admin_username.short_description = 'Usuário'

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        group_name = 'Commons Users'
        group, created = Group.objects.get_or_create(name=group_name)
        obj.groups.add(group)
        obj.save()

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
