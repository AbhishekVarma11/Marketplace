from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path,include
from .forms import LoginForm
from . import views 
app_name='webapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='webapp/login.html',authentication_form=LoginForm),name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='webapp:login'), name='logout'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
