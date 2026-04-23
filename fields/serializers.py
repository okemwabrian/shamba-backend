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
# 🔥 Custom JWT Serializer (FIXED)
# -------------------------
class CustomTokenSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        user = self.user

        # ✅ FIX: Ensure admin is correctly detected
        if user.is_staff or user.is_superuser:
            role = "ADMIN"
        else:
            role = user.role if hasattr(user, 'role') and user.role else "AGENT"

        data["role"] = role
        data["username"] = user.username

        return data