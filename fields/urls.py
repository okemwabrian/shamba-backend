from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FieldViewSet, FieldUpdateViewSet, DashboardSummaryView, CustomTokenView

router = DefaultRouter()

router.register(r'fields', FieldViewSet, basename='field')
router.register(r'updates', FieldUpdateViewSet, basename='update')

urlpatterns = [
    path('', include(router.urls)),

    # ✅ Dashboard
    path('dashboard/summary/', DashboardSummaryView.as_view()),

    # 🔥 Custom JWT login
    path('token/', CustomTokenView.as_view()),
]