from drf_yasg import openapi

possibilities = {
    "200": openapi.Response(
        description="custom 200 description",
        examples={
            "application/json": {
                "gateways": [],
                "message": "ok"
            }
        }
    ),
    "202": openapi.Response(
        description="custom 202 description",
        examples={
            "application/json": {
                "message": "accepted"
            }
        }
    ),
    "204": openapi.Response(
        description="custom 204 description",
        examples={
            "application/json": {
                "message": "not found"
            }
        }
    ),
    "401": openapi.Response(
        description="custom 401 description",
        examples={
            "application/json": {
                "detail": "Invalid token."
            }
        }
    ),
    "400": openapi.Response(
        description="custom 400 description",
        examples={
            "application/json": {
                "message": "abstence of parameters"
            }
        }
    ),
}