"""logopedasur URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from logopedasur.main import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login_view, name='login_view'),
    url(r'^logout/', views.logout_view, name='logout_view'),
    url(r'^admin/', admin.site.urls),
    url(r'', include('logopedasur.pacientes.urls')),
    url(r'', include('logopedasur.sesiones.urls')),
    url(r'', include('logopedasur.facturacion.urls')),
    url(r'', include('logopedasur.terapeutas.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
