from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *

class PerevalView(APIView):
    # Метод с помощью которого будет пополняться информацию в таблицах базы данных
    def get(self, request):
        username = request.user.username
        queryset = dbPereval.objects.filter(raw_data__user__contains={'id': username})
        serializer = PerevalSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PerevalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            result = {"status": "200", "message": f'Перевал добавлен.'}
            return Response(result, status=200)
        else:
            result = {"status": "400", "message": f'{serializer.errors}'}
            return Response(result, status=400)
