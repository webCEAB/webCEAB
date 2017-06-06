from django.conf.urls import include, url
from django.contrib import admin
from siad.views import atributos_meta
from siad import views
from promotoria import views
from controlescolar import views
from contabilidad import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'CEABweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'', include('main.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('siad.urls')),
    url(r'^meta/',atributos_meta),
	url(r'^formulario_buscar/$', views.formulario_buscar),
	url(r'^buscar/$', views.buscar),
	url(r'^contactos/$', views.contactos),
]
