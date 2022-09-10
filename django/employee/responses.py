from drf_yasg import openapi
from common.swaggerresponse import possibilities

EmployeeResponseList = {
    "200": openapi.Response(
        description="custom 200 description",
        examples={
            "application/json": {
                "employees": [],
                "message": "ok"
            }
        }
    ),
}
EmployeeResponseList["204"] = possibilities["204"] # insert the commom response

EmployeeResponseRetrieve = {
    "200": openapi.Response(
        description="custom 200 description",
        examples={
            "application/json": {
                "employee": {},
                "message": "ok"
            }
        }
    ),
}
EmployeeResponseRetrieve["401"] = possibilities["401"] # insert the commom response
EmployeeResponseRetrieve["204"] = possibilities["204"] # insert the commom response

EmployeeResponseDestroy = {}
EmployeeResponseDestroy["204"] = possibilities["204"] # insert the commom response
EmployeeResponseDestroy["202"] = possibilities["202"] # insert the commom response