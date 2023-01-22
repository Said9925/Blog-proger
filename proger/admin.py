from django.contrib import admin

from proger.models import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'create_at', 'photo')
    list_display_links = ('title',)
    search_fields = ('title',)
    list_filter = ('create_at',)
    prepopulated_fields = {"slug":("title",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {"slug":("name",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)