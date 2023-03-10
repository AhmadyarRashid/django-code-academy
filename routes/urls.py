from django.urls import path

from . import views

urlpatterns = [
  path('', views.HomeView.as_view(), name='home'),
  path('lines/', views.LinesView.as_view(), name="lines"),
  path('line/new/', views.CreateLineView.as_view(), name="create_line"),
  path('line/<pk>/update', views.UpdateLineView.as_view(), name="update_line"),
  path('line/<pk>/delete/', views.DeleteLineView.as_view(), name="delete_line")
]
