from rest_framework import serializers
from tegerte.models import *
from django.contrib.auth.models import User


class AcudienteSerializer(serializers.ModelSerializer):
 class Meta:
    model = Acudiente
    fields = ('nombre', 'apellidos', 'documento', 'telefono', 'email', 'direccion', 'fecha_creacion','id')


class VusuarioSerializer(serializers.ModelSerializer):
 class Meta:
    model = Vusuario
    fields = ('nombre', 'apellidos', 'documento', 'telefono', 'email', 'direccion', 'fecha_creacion','id')


class EntidadSerializer(serializers.ModelSerializer):
 class Meta:
    model = Entidad
    fields = ('entidad','ubicacion','direccion','telefono','fecha_creacion','id')


class TipoSucesoSerializer(serializers.ModelSerializer):
 class Meta:
    model = TipoSuceso
    fields = ('tiposuceso','fecha_creacion','id')

class AgresorSerializer(serializers.ModelSerializer):
 class Meta:
    model = Agresor
    fields = ('nombre', 'apellidos', 'documento', 'telefono','fecha_creacion','id')

class SucesoSerializer(serializers.ModelSerializer):
 class Meta:
    model = Suceso
    fields = ('inicio','ubicacion','agresor ','acudiente','tiposuceso','id')

class UsuarioSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True,
    source="user.username")
    password = serializers.CharField(write_only=True,
    source="user.password")
    nombre = serializers.CharField(required=False)
    apellido = serializers.CharField(required=False)
    correo = serializers.CharField(required=False)
    fecha_nacimiento = serializers.DateField(required=False)
    perfil = serializers.CharField(required=False)
    #category_name = serializers.RelatedField(source='category',read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'nombre', 'apellido','correo', 'fecha_nacimiento', 'perfil')
    def create(self, validated_data, instance=None):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        user.set_password(user_data['password'])
        user.save()
        Usuario.objects.update_or_create(user=user,**validated_data)
        usuario = Usuario.objects.get(user=user)
        return usuario
