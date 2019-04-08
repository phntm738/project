from django.contrib.auth import views as auth_views
from django.urls import path, re_path, include
from .forms import LoginForm

from . import views

urlpatterns = [
    path('test', views.test),
    path('test1', views.test1),
]


authpatterns = [
    path('login', auth_views.LoginView.as_view(template_name='main/login_form.html', form_class=LoginForm,
                                               redirect_authenticated_user=True), name='login'),
    path('do-logout', auth_views.LogoutView.as_view(), name='logout'),
    path('register', views.RegistrationView.as_view(), name='register'),
    path('reset', auth_views.PasswordResetView.as_view(template_name='main/password_reset_form.html', )),
    path('done', auth_views.PasswordResetDoneView.as_view(template_name='main/password_reset_done.html'), name='password_reset_done'),
    re_path(r'^confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            auth_views.PasswordResetConfirmView.as_view(success_url='/main', template_name='main/password_reset_confirm.html'), name='password_reset_confirm')
]


profpatterns = [
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('avatar/', include('avatar.urls'), name='avatar'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            views.activate, name='activate'),
]


edupatterns = [
    path('', views.index, name='index'),
    path('lang/<str:language_name>', views.language_page, name='language'),
    path('lang/<str:language_name>/sec/<str:section_name>', views.section_page, name='section'),
    path('lang/<str:language_name>/sec/<str:section_name>/les/<int:lesson_order>', views.lesson_page, name='lesson'),
    path('lang/<str:language_name>/game', views.GameView.as_view(), name='game')
]


urlpatterns += authpatterns
urlpatterns += profpatterns
urlpatterns += edupatterns
