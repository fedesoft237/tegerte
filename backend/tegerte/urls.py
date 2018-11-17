from django.conf.urls import url
from tegerte import views

urlpatterns = [
 url(r'^Acudiente/$', views.AcudienteList.as_view()),
 url(r'^Acudiente/(?P<pk>[0-9]+)/$', views.AcudienteDetail.as_view()),

 url(r'^Vusuario/$', views.VusuarioList.as_view()),
 url(r'^Vusuario/(?P<pk>[0-9]+)/$', views.VusuarioDetail.as_view()),

 url(r'^Entidad/$', views.EntidadList.as_view()),
 url(r'^Entidad/(?P<pk>[0-9]+)/$', views.EntidadDetail.as_view()),

 url(r'^TipoSuceso/$', views.TipoSucesoList.as_view()),
 url(r'^TipoSuceso/(?P<pk>[0-9]+)/$', views.TipoSucesoDetail.as_view()),

 url(r'^Agresor/$', views.AgresorList.as_view()),
 url(r'^Agresor/(?P<pk>[0-9]+)/$', views.AgresorDetail.as_view()),

 url(r'^Suceso/$', views.SucesoList.as_view()),
 url(r'^Suceso/(?P<pk>[0-9]+)/$', views.SucesoDetail.as_view()),

 url(r'^usuarios/$', views.UsuarioList.as_view()),
 url(r'^usuarios/(?P<pk>[0-9]+)/$', views.UsuarioDetail.as_view()),
 
]