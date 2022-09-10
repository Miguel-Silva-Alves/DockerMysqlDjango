from rest_framework.response import Response
from rest_framework import status


def BadRequest(message='abstence of parameters'):
    return Response(status=status.HTTP_400_BAD_REQUEST, data={'message':message})

def InternalError(error):
    return Response(data={'message': error}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def CreatedRequest():
    return Response(data={'message':'created'}, status=status.HTTP_201_CREATED)

def ResponseDefault(message='ok', data={}):
    data['message'] = message
    return Response(status=status.HTTP_200_OK, data=data)

def NotFound(message = 'not found'):
    return Response(data={'message': message}, status=status.HTTP_204_NO_CONTENT)

def ChangeRequest(message = 'changed'):
    return Response(data={'message': message}, status=status.HTTP_200_OK)

def UnauthorizedRequest():
    return Response(status=status.HTTP_401_UNAUTHORIZED, data={'message':'not allowed'})

def AcceptedRequest():
    return Response(status=status.HTTP_202_ACCEPTED)