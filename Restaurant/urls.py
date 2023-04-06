from django.urls import path
from .views import menuView,bookingView,index,SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', index, name='home'),
    path('menu/', menuView.as_view()),
    path('booking/', bookingView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),

]
