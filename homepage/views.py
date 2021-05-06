from .models import Hadithi, DemoStories
from django.contrib.auth.models import User
from .serializers import HadithiSerializer, UserSerializer, DemoSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework import permissions
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Users': reverse('users', request=request, format=format),
        'Stories': reverse('home', request=request, format=format),
    })

#check or use format in frontend
class Stories(APIView):
    def get(self, request, format=None):
        stories = Hadithi.objects.all()
        serializer = HadithiSerializer(stories, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HadithiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #test serializers error dict


class Story(APIView):
    def get_object(self, pk):
        try:
            return Hadithi.objects.get(id=pk)
        except Hadithi.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        story = self.get_object(pk)
        serializer = HadithiSerializer(story)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        story = self.get_object(pk)
        serializer = HadithiSerializer(story, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        story = self.get_object(pk)
        story.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DemoStories(generics.ListAPIView):
    queryset = DemoStories.objects.all()
    serializer_class = DemoSerializer