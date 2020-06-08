# customers/backends.py
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

from college.models import CollegeAdmin

class CollegeBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        username = kwargs['username']
        password = kwargs['password']
        try:
            user = User.objects.get(username=username)
            if user.check_password(password) is True:
                college_admin = CollegeAdmin.objects.get(user=user)
                if college_admin:
                    return user
        except college_admin.DoesNotExist:
            pass
        except:
            pass
