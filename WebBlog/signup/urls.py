from django.urls import path, include
from .views import UserEditView, UserRegisterView

urlpatterns = [ 
   
   path('register/',UserRegisterView.as_view(),name = 'register'),
   path('edit_profile/',UserEditView.as_view(),name = 'edit_profile'),

   ]
