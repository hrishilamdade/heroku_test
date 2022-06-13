from django.shortcuts import render
from rest_framework.viewsets import generics# Create your views here.
from .serializers import *
from rest_framework.response import Response

class TestView(generics.GenericAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()
    def get(self, request):
        data = self.serializer_class(self.get_queryset(), many=True).data

        return Response(data)

    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
