from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from apps.services import serializers, models

class ListServices(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request, *args, **kwargs):
        services = models.Service.objects.all()
        seriazlier = serializers.ServiceSerializer(services, many=True)
        return Response(seriazlier.data)

    def post(self, request):
        reg_serializer = serializers.ServiceSerializer(data=request.data)
        if reg_serializer.is_valid():
            new_service = reg_serializer.save()
            if new_service:
                return Response(status=status.HTTP_201_CREATED)
        
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServiceDetailView(APIView):
    def get(self, request, pk):
        services = models.Service.objects.filter(id=pk)
        seriazlier = serializers.ServiceSerializer(services, many=True)
        return Response(seriazlier.data)
        
    def put(self, request, pk, format=None):        
        service = models.Service.objects.filter(id=pk).first()
        serializer = serializers.ServiceSerializer(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        service = models.Service.objects.filter(id=pk)
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ListOrderItems(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        items = models.ServiceOrderItem.objects.all()
        seriazlier = serializers.ServiceOrderItemSerializer(items, many=True)
        return Response(seriazlier.data)

    def post(self, request):
        reg_serializer = serializers.ServiceOrderItemSerializer(data=request.data)
        if reg_serializer.is_valid():
            new_item = reg_serializer.save()
            if new_item:
                return Response(status=status.HTTP_201_CREATED)
        
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServiceOrderItemDetailView(APIView):
    def put(self, request, pk, format=None):        
        item = models.ServiceOrderItem.objects.filter(id=pk).first()
        serializer = serializers.ServiceOrderItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        item = models.ServiceOrderItem.objects.filter(id=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ListServiceTypes(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        service_types = models.ServiceType.objects.all()
        seriazlier = serializers.ServiceTypeSerializer(service_types, many=True)
        return Response(seriazlier.data)

# class TeamDetailView(APIView):
#     def get(self, request, pk):
#         teams = models.Team.objects.filter(id=pk).first()
#         seriazlier = serializers.TeamSerializer(teams, many=True)
#         return Response(seriazlier.data)
        
#     def put(self, request, pk, format=None):        
#         team = models.Team.objects.filter(id=pk).first()
#         serializer = serializers.TeamSerializer(team, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         team = models.Team.objects.filter(id=pk)
#         team.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)