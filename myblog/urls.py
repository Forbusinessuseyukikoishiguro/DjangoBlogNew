from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # ここを変更: as_viewの引数にredirect_authenticated_userとnext_pageを追加
    path('logout/', auth_views.LogoutView.as_view(
        template_name='users/logout.html',
        next_page='login'
    ), name='logout'),
    path('', include('blog.urls')),
]