from flask import Response

def get_as_response(data, success=True):
    return Response(response=data, headers={'content-type': 'application/json'}, status=200 if success else 400)