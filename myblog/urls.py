from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

# LogoutViewを拡張してGETリクエストを許可するクラスを作成
class CustomLogoutView(auth_views.LogoutView):
    http_method_names = ['get', 'post']

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # カスタムログアウトビューを使用
    path('logout/', CustomLogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('myblog/', include('blog.urls')),
]

# 開発環境でのみメディアファイルのURLを追加
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)