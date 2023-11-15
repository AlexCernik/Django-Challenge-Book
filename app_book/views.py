from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Book
from .serializers import BookSerializer

class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('-id')
    permission_classes = (IsAuthenticated,)
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset.filter(user=self.request.user)
    
    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, user=self.request.user, pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data)
    
    def update(self, request, pk):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk):
        instance = self.get_object()
        instance.delete()
        return Response({'detail': 'Libro eliminado.'})