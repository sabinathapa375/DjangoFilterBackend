from apiapp import views
from django.urls import path, include

urlpatterns = [
    path('studentapi/', views.StudentList.as_view(), name='studentapi'),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
