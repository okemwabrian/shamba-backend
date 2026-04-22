from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Field, FieldUpdate


# -------------------------
# Field Serializer
# -------------------------
class FieldSerializer(serializers.ModelSerializer):
    status = serializers.ReadOnlyField()

    class Meta:
        model = Field
        fields = '__all__'


# -------------------------
# Field Update Serializer
# -------------------------
class FieldUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldUpdate
        fields = '__all__'
        read_only_fields = ['agent']


# -------------------------
# 🔥 Custom JWT Serializer
# -------------------------
class CustomTokenSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # ✅ Add extra user info
        data["role"] = self.user.role
        data["username"] = self.user.username

        return data