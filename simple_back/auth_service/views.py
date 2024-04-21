import logging
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from .models import CustomUser
from .serializers import CustomUserCreateSerializer

logger = logging.getLogger(__name__)


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserCreateSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]

        if self.action in ['list']:
            permission_classes.append(IsAdminUser)

        return [permission() for permission in permission_classes]

