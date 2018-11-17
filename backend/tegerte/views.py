from django.shortcuts import render
from tegerte.models import *
from rest_framework import generics
from .serializers import *
from rest_framework.decorators import permission_classes
from tegerte.permissions import IsPostOrIsAuthenticated

#Con def creamos funciones
def principal(request):
    instituciones = Alumno.objects.all()
    return render(request,'principal.html', {'Loquevoyaenviar' :tegerte})

#Acudiente
class AcudienteList(generics.ListCreateAPIView):
 serializer_class = AcudienteSerializer
 queryset = Acudiente.objects.all()
class AcudienteDetail(generics.RetrieveUpdateDestroyAPIView):
 serializer_class = AcudienteSerializer
 queryset = Acudiente.objects.all()

#Vusuario
class VusuarioList(generics.ListCreateAPIView):
 serializer_class = VusuarioSerializer
 queryset = Vusuario.objects.all()
class VusuarioDetail(generics.RetrieveUpdateDestroyAPIView):
 serializer_class = VusuarioSerializer
 queryset = Vusuario.objects.all()

 #Entidad

class EntidadList(generics.ListCreateAPIView):
 serializer_class = EntidadSerializer
 queryset = Entidad.objects.all()
class EntidadDetail(generics.RetrieveUpdateDestroyAPIView):
 serializer_class = EntidadSerializer
 queryset = Entidad.objects.all()

 #TipoSuceso

class TipoSucesoList(generics.ListCreateAPIView):
 serializer_class = TipoSucesoSerializer
 queryset = TipoSuceso.objects.all()
class TipoSucesoDetail(generics.RetrieveUpdateDestroyAPIView):
 serializer_class = TipoSucesoSerializer
 queryset = TipoSuceso.objects.all()

 #Agresor

class AgresorList(generics.ListCreateAPIView):
 serializer_class = AgresorSerializer
 queryset = Agresor.objects.all()
class AgresorDetail(generics.RetrieveUpdateDestroyAPIView):
 serializer_class = AgresorSerializer
 queryset = Agresor.objects.all()
 
 #Suceso

class SucesoList(generics.ListCreateAPIView):
 serializer_class = SucesoSerializer
 queryset = Suceso.objects.all()
class SucesoDetail(generics.RetrieveUpdateDestroyAPIView):
 serializer_class = SucesoSerializer
 queryset = Suceso.objects.all()

#usuario

@permission_classes((IsPostOrIsAuthenticated, ))
class UsuarioList(generics.ListCreateAPIView):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
