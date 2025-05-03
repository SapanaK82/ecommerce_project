from django.contrib.auth.backends import ModelBackend
from .models import User

class EmailAuthBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = User.objects.get(email=email)
            if user.password(password):
                return user
        except User.DoesNotExist:
            return None