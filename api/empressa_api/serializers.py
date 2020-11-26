from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Empressa

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','username', 'email'] 

class EmpressaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Empressa
        fields = ['url', 'nome_empressa', 'endereco', 'mail', 'contato', 'avalicao']