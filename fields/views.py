from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied

from rest_framework_simplejwt.views import TokenObtainPairView  # ✅ NEW
from .serializers import FieldSerializer, FieldUpdateSerializer, CustomTokenSerializer  # ✅ UPDATED

from .models import Field, FieldUpdate


# -------------------------
# 🔥 Custom Token View
# -------------------------
class CustomTokenView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer


# -------------------------
# Permissions
# -------------------------
class IsAdminOrAgent(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated


# -------------------------
# Field ViewSet
# -------------------------
class FieldViewSet(viewsets.ModelViewSet):
    serializer_class = FieldSerializer
    permission_classes = [IsAdminOrAgent]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff or user.role == 'ADMIN':
            return Field.objects.all()

        return Field.objects.filter(assigned_agent=user)


# -------------------------
# Field Update ViewSet
# -------------------------
class FieldUpdateViewSet(viewsets.ModelViewSet):
    serializer_class = FieldUpdateSerializer
    permission_classes = [IsAdminOrAgent]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff or user.role == 'ADMIN':
            return FieldUpdate.objects.all()

        return FieldUpdate.objects.filter(agent=user)

    def perform_create(self, serializer):
        update = serializer.save(agent=self.request.user)
        field = update.field

        if not (self.request.user.is_staff or self.request.user.role == 'ADMIN'):
            if field.assigned_agent != self.request.user:
                raise PermissionDenied("You can only update your assigned fields")

        field.current_stage = update.stage
        field.save()


# -------------------------
# Dashboard Summary
# -------------------------
class DashboardSummaryView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user

        if user.is_staff or user.role == 'ADMIN':
            fields = Field.objects.all()
        else:
            fields = Field.objects.filter(assigned_agent=user)

        total = fields.count()
        active = sum(1 for f in fields if f.status == 'Active')
        at_risk = sum(1 for f in fields if f.status == 'At Risk')
        completed = sum(1 for f in fields if f.status == 'Completed')

        return Response({
            "total": total,
            "active": active,
            "at_risk": at_risk,
            "completed": completed
        })