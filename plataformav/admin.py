from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
from plataformav.models import Account, Post, PostFeed, Comment

class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'cpf', 'dateBirth', 'cellphone')
    list_display_links = ('id', 'name')
    list_per_page = 20
    search_fields = ('name',)

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
