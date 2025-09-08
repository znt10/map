from django.contrib import admin
from django.urls import path, include
from artistas.views import LoginView,Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name='login'), 
    path('home/', Home.as_view(), name='home'),
    path('accounts/', include('allauth.urls')),  
]
