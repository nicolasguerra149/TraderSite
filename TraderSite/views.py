from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from TraderSite.serializers import TestSerializer, UserSerializer, GroupSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
import datetime as dt
dt.datetime.now()

@api_view(['GET', 'POST'])
def test_post_request(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        # TODO: Fill in later
        return Response(None)

    elif request.method == 'POST':
        print("Request data", request.data)
        #serializer = TestSerializer(data=request.data)
        test_obj = Test(request.data)
        serializer = TestSerializer(test_obj)
        print("Serializer Data", serializer.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # return Response(serializer.data)
        print(type(serializer.data))
        #return render(request, 'main.html', {"test_number" : request.data})
        return render(request, 'main.html', serializer.data)


class Test(object):
    def __init__(self, test_number):
        self.test_number = test_number
        self.dt = dt.datetime.now()
        print(self.dt)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
