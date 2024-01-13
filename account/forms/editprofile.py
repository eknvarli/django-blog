from django.contrib.auth.forms import UserChangeForm
from account.models import CustomUser

class EditProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'avatar')