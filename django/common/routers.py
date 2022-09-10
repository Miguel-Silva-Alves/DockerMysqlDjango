from rest_framework import routers

def getRouter():
    return routers.DefaultRouter(trailing_slash=False)