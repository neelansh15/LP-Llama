
from rest_framework import serializers

from lp_lama.models import *


class Block(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = '__all__'


class Exchange(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        fields = '__all__'


class Lp(serializers.ModelSerializer):
    class Meta:
        model = Lp
        fields = '__all__'
