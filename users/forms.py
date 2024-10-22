from django.contrib.auth.forms import UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']