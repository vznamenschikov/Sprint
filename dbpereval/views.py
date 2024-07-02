from rest_framework.views import APIView
from rest_framework import viewsets, generics, status
from rest_framework.response import Response

from .serializers import *
from .models import *


class PerevalRecordView(APIView):
    # Просмотр и редактирование записей по ID   'submitData/<int:pk>', PerevalRecordView.as_view()
    def get(self, request, pk):
        if dbPereval.objects.filter(id=pk).exists():
            pereval = dbPereval.objects.get(id=pk)
            return Response(self.prepare_result(pereval))
        else:
            result = {"status": "503", "message": "Record not found"}
            return Response(result, status=503)

    def put(self, request, pk):
        if dbPereval.objects.filter(id=pk).exists():
            pereval = dbPereval.objects.get(id=pk)
            serializer = PerevalSerializer(pereval, data=request.data)
            if serializer.is_valid():
                pereval = serializer.save()
                result = {"status": "200", "message": f'pereval updated. Id {pereval.pk}'}
                return Response(result, status=200)
            else:
                result = {"status": "400", "message": f'{serializer.errors}'}
                return Response(result, status=400)
        else:
            result = {"status": "503", "message": "Record not found"}
            return Response(result, status=503)

    def prepare_result(self, pereval):
        serializer = PerevalSerializer(pereval, many=False)
        return serializer.data


class PerevalStatusView(PerevalRecordView):
    # Просмотр статуса      'submitData/<int:pk>/status', PerevalStatusView.as_view()
    def prepare_result(self, pereval):
        result = {"status": f'{pereval.status}'}
        return result


class PerevalView(APIView):
    # Обновление данных     'submitData/', PerevalView.as_view()
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

