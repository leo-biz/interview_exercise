from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .models import SecurityFeature
from .serializers import SecurityFeatureSerializer

@api_view(['GET', 'POST'])
def security_features_list(request):
    if request.method == 'GET':
        security_features = SecurityFeature.objects.all()
        serializer = SecurityFeatureSerializer(security_features, many=True)
        return JsonResponse({'results':serializer.data})
    elif request.method == 'POST':
        many = isinstance(request.data, list)
        serializer = SecurityFeatureSerializer(data=request.data, many=many)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'response':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
