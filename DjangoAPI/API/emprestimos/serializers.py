from rest_framework import serializers
from .models import aprovado

class aprovadoSerializers(serializers.ModelSerializer):
	class Meta:
		model=aprovado
		fields='__all__'
