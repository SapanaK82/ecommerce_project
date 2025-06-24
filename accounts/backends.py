# from django.contrib.auth.backends import ModelBackend
# from .models import User

# class UsernameAuthBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None):
#         try:
#             user = User.objects.get(username=username)
#             if user.password(password):
#                 return user
#         except User.DoesNotExist:
#             return None