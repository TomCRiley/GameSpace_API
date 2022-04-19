from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from django.conf import settings  # for the secret key
import jwt
User = get_user_model()

# this whole file is similar to the secureRoute middleware file in Express


class JWTAuthentication(BasicAuthentication):
    def authenticate(self, request):
        print("called function")
        header = request.headers.get('Authorization')
        if not header:
            return None
        if not header.startswith('Bearer'):
            raise PermissionDenied({'message': 'Invalid authorization header'})
        token = header.replace('Bearer ', '')
        print(token)
        try:
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(pk=payload.get('sub'))
        except jwt.exceptions.InvalidTokenError:
            raise PermissionDenied({'message': 'Invalid Token'})
        except User.DoesNotExist:
            raise PermissionDenied({'message': 'User not found'})
        return (user, token)
