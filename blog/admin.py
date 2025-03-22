from django.contrib import admin
from .models import Post, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'post_count')
    search_fields = ('name', 'description')
    
    def post_count(self, obj):
        return obj.posts.count()
    post_count.short_description = '投稿数'

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted', 'display_categories', 'has_audio', 'has_youtube')
    list_filter = ('date_posted', 'author', 'categories')
    search_fields = ('title', 'content')
    date_hierarchy = 'date_posted'
    ordering = ('-date_posted',)
    filter_horizontal = ('categories',)  # 多対多フィールドの編集を改善
    
    def display_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    display_categories.short_description = 'カテゴリ'
    
    def has_audio(self, obj):
        return bool(obj.audio_file)
    has_audio.boolean = True
    
    def has_youtube(self, obj):
        return bool(obj.youtube_url)
    has_youtube.boolean = True

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)