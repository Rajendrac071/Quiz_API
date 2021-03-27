from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm, UserChangeForm

class UserAdmin(UserAdmin):
    add_form        = UserCreationForm
    form            = UserChangeForm
    model           = User
    list_display    = ('username', 'name', 'email', 'is_active')
    list_filter     = ('username', 'name', 'email', 'is_active')
    fieldsets       = (
                        (None, {'fields':('username', 'name', 'email','password')}),
                        ('Permissions', {'fields':('is_staff', 'is_active')})
    )
    search_fields   = ('username',)
    ordering        = ('username',)

admin.site.register(User, UserAdmin)
