from .models import Task
from .serializer import TaskSerializer

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        task = super().get_object()

        if task.user != self.request.user:
            self.permission_denied(self.request)

        return task
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user, completed__exact=False).order_by('-important')

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['user'] = request.user.id
        serializer = self.get_serializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Task created successfully',
                'task': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False)
    def completed_tasks(self, request):
        tasks = Task.objects.filter(user=request.user, completed__exact=True)
        serializer = self.serializer_class(tasks, many=True)
        return Response(serializer.data)