from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name = 'about'),
  path('horses/', views.horses_index, name = 'horses_index'),
  path('horses/<int:horse_id>/', views.horses_detail, name='horses_detail'),
  path('horses/create/', views.HorseCreate.as_view(), name='horses_create'),
  path('horses/<int:pk>/update/', views.HorseUpdate.as_view(), name='horses_update'),
  path('horses/<int:pk>/delete/', views.HorseDelete.as_view(), name='horses_delete'),
  path('horses/<int:horse_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
  path('toys/', views.ToyList.as_view(), name='toys_index'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
  path('horses/<int:horse_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
  path('accounts/signup/', views.signup, name='signup'),
]