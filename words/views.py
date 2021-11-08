from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse

"""
Tutaj dokładacie nowe funkcje, które potem montujecie w pliku urls.py
"""


def index(request):
    return HttpResponse("Hello, world. You're at the words index.")


def words(request):
    data = {'words': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt...'}
    return JsonResponse(data)


def czas(request):
    data = {'czas': 'TODO'}
    return JsonResponse(data)


def sentencje(request):
    sentencje = [
        'aaaa',
        'bvbbbb'
    ]
    return JsonResponse(sentencje[0])


class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)


@api_view(['GET', 'POST'])
def test_get_post(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})
