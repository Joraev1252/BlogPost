from django.urls import path, include
from account.api.views import accounts_view, account_register, account_login, account_logout, update_account


app_name = 'account_api'

urlpatterns = [
    path('account/', accounts_view),
    path('account_update/', update_account),
    path('register/', account_register),
    path('login/', account_login),
    path('logout/', account_logout)
]



