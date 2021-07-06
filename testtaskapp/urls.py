from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('save_pdf', views.save_pdf, name="save_pdf")
]