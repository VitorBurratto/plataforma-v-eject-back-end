from django.contrib import admin
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