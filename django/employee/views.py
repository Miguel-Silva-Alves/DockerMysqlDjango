from rest_framework.viewsets import ViewSet

from django.forms.models import model_to_dict

# Models
from employee.models import Employee

# Swagger
from drf_yasg.utils import swagger_auto_schema

# Serializer
from employee.serializer import EmployeeSerializer

# Response
from common.response import BadRequest, InternalError, CreatedRequest, ResponseDefault, NotFound, AcceptedRequest
from employee.responses import EmployeeResponseList, EmployeeResponseRetrieve, EmployeeResponseDestroy

# Create your views here.
class EmployeeView(ViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    # Create some employee
    @swagger_auto_schema(request_body=EmployeeSerializer)
    def create(self, request, *args, **kwargs):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            
            first_name = request.data.get('first_name')
            last_name = request.data.get('last_name')
            email = request.data.get('email')
            department = request.data.get('department')

            # register a new user
            try:
                Employee.objects.create(
                    first_name = first_name,
                    email = email,
                    last_name = last_name,
                    department = department
                )
            except Exception as e:
                return InternalError(str(e))

            return CreatedRequest()

        return BadRequest()

    # List all employees
    @swagger_auto_schema(responses=EmployeeResponseList)
    def list(self, request):
        all_employees = Employee.objects.values()

        if all_employees:
            print(list(all_employees))
            return ResponseDefault(data={'employees': list(all_employees)})
        return NotFound()
    
    # Retrieve an specific employee
    @swagger_auto_schema(responses=EmployeeResponseRetrieve)
    def retrieve(self, request, pk=None):
        employee = Employee.objects.filter(pk=pk).first()
        if employee == None:
            return NotFound()
        return ResponseDefault(message='ok', data={'employee': model_to_dict(employee)})
    
    # Update an specific employee
    @swagger_auto_schema(request_body=EmployeeSerializer)
    def update(self, request, pk):
        employee = Employee.objects.get(pk=pk)
        data = EmployeeSerializer(instance=employee, data=request.data)
  
        if data.is_valid():
            data.save()
            employeeUpdated = Employee.objects.get(pk=pk)
            return ResponseDefault(message='ok', data={'employee': model_to_dict(employeeUpdated)})
        return BadRequest()

    # Destroy an specific employee
    @swagger_auto_schema(responses=EmployeeResponseDestroy)
    def destroy(self, request, pk=None):
        employee = Employee.objects.get(pk=pk)
        if employee:
            employee.delete()
            return AcceptedRequest()
        return NotFound()
