from django.contrib import admin
from account.models import Account, MyAccountManage


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'age')
    list_display_links = ('id', 'email')
    search_fields = ('id', 'f_name', 'age')
    list_filter = ('id',)


admin.site.register(Account, TodoAdmin)


