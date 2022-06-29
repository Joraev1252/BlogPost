from django.urls import path
from account.views import *

app_name = 'account'

urlpatterns = [
    path('home/', home, name='home_page'),
    path('signup/', registration_view, name='signup'),
    path('', authentication, name='signin'),
    path('signout/', signout_view, name='signout'),
    path('update/<int:pk>/', update_account, name='update_account'),

]
