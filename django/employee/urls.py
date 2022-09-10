from django.urls import path, include

from common.routers import getRouter

# Views
from employee.views import EmployeeView

router = getRouter()

router.register(r'employee', EmployeeView)
urlpatterns = [
    path('', include(router.urls)),
]