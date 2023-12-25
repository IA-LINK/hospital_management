from django.urls import path
from .views import DepartmentListView, DoctorDetailView

urlpatterns = [
    path('departments/', DepartmentListView.as_view(), name='department_list'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
]