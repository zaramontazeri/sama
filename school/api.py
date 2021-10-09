from django.db.models.query import QuerySet
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models
from . import serializers
from rest_framework import status, viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend

class GetParentWithUserView(APIView):
    """View to get parent id . you must authenticate  """
    
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        user = request.user
        try:
            parent = models.Parent.objects.get(user=user)
        except models.Parent.DoesNotExist:
            return Response({
                'detail': 'parent with this user does not exist',
                'code': 'parent_not_exist',
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
                "parent_id":parent.id
            }, status=status.HTTP_200_OK)

class ParentViewSet(viewsets.ModelViewSet):
    """ViewSet for the Parent class"""

    queryset = models.Parent.objects.all()
    serializer_class = serializers.ParentSerializer
    permission_classes = [permissions.IsAuthenticated]
    def create(self, request, *args, **kwargs):
        data=request.data
        print(request.user.id)

        data["user"] = request.user.id
        print(request.user.id)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data=request.data
        data["user"] = request.user.id
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

class StudentViewSet(viewsets.ModelViewSet):
    """ViewSet for the Student class"""
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    def get_queryset(self):
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )

        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            if(self.request.user.is_superuser):
                queryset = queryset.all()
            else:
                try:
                    parent = self.request.user.parent
                    if parent:
                        queryset = queryset.filter(parent=parent)
                except  :
                    pass
        return queryset

class LevelViewSet(viewsets.ModelViewSet):
    """ViewSet for the School class"""

    queryset = models.Level.objects.all()
    serializer_class = serializers.LevelSerializer
    permission_classes = [permissions.IsAuthenticated]

# class CityViewSet(viewsets.ModelViewSet):
#     """ViewSet for the City class"""

#     queryset = models.City.objects.all()
#     serializer_class = serializers.CitySerializer
#     permission_classes = [permissions.IsAuthenticated]

class RegionViewSet(viewsets.ModelViewSet):
    """ViewSet for the Region class"""

    queryset = models.Region.objects.all()
    serializer_class = serializers.RegionSerializer
    permission_classes = [permissions.IsAuthenticated]

class SchoolViewSet(viewsets.ModelViewSet):
    """ViewSet for the School class"""

    queryset = models.School.objects.all()
    serializer_class = serializers.SchoolSerializer
    permission_classes = [permissions.IsAuthenticated]