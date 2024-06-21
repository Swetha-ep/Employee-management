from django.urls import path
from . import views


urlpatterns = [
  path('',views.home_page,name='homepage'),
  path('add/',views.add_emp,name='add'),
  path('remove/',views.remove_emp,name='remove'),
  path('view/',views.view_emp,name='view'),
  path('list/',views.list_emp,name='list'),
]