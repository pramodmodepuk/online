from django.forms import ModelForm
from django.contrib.auth.models import User


class RegesterForm(ModelForm):
    class Meta:
        model = User
        exclude = ['is_staff', 'is_superuser', 'is_active']