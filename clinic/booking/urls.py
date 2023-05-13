from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('booking', views.booking, name='booking'),
    path('booking-submit', views.bookingSubmit, name='bookingSubmit'),
    path('user-panel', views.userPanel, name='userPanel'),
    path('user-update/<int:id>', views.userUpdate, name='userUpdate'),
    path('user-update-submit/<int:id>', views.userUpdateSubmit, name='userUpdateSubmit'),
    path('staff-panel', views.staffPanel, name='staffPanel'),
    path('password_reset_form', views.password_reset_form, name='password_reset_form'),
    path('', views.delete, name='delete'),
    path('portofolio', views.portofolio, name='portofolio'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('delete-item/<int:id>/',views.deleteitem, name ="delete-item"),  
]
