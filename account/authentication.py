from django.contrib.auth.models import User


# authenticates using email
class EmailAuthBackend(object):
    # retrieve user with a given email and check its password
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    # get a user through id
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
