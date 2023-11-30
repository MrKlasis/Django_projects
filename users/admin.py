from django.contrib import admin

from users.models import User

# admin.site.register(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'email_verify', 'token')
    list_filter = ('email_verify',)
    search_fields = ('email', 'email_verify')