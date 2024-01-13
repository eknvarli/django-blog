from django.contrib.auth.forms import UserCreationForm
from account.models import CustomUser

class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username','email','first_name','last_name','password1','password2')