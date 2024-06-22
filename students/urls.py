from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('students/', views.StudentListView.as_view(), name='student_list'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('students/create/', views.StudentCreateView.as_view(), name='student_create'),
    path('students/update/<int:pk>/', views.StudentUpdateView.as_view(), name='student_update'),
    path('students/delete/<int:pk>/', views.StudentDeleteView.as_view(), name='student_delete'),

    path('courses/', views.CourseListView.as_view(), name='course_list'),
    path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('courses/create/', views.CourseCreateView.as_view(), name='course_create'),
    path('courses/update/<int:pk>/', views.CourseUpdateView.as_view(), name='course_update'),
    path('courses/delete/<int:pk>/', views.CourseDeleteView.as_view(), name='course_delete'),

    path('enrollments/', views.EnrollmentListView.as_view(), name='enrollment_list'),
    path('enrollments/<int:pk>/', views.EnrollmentDetailView.as_view(), name='enrollment_detail'),
    path('enrollments/create/', views.EnrollmentCreateView.as_view(), name='enrollment_create'),
    path('enrollments/update/<int:pk>/', views.EnrollmentUpdateView.as_view(), name='enrollment_update'),
    path('enrollments/delete/<int:pk>/', views.EnrollmentDeleteView.as_view(), name='enrollment_delete'),

    path('instructors/', views.InstructorListView.as_view(), name='instructor_list'),
    path('instructors/<int:pk>/', views.InstructorDetailView.as_view(), name='instructor_detail'),
    path('instructors/create/', views.InstructorCreateView.as_view(), name='instructor_create'),
    path('instructors/update/<int:pk>/', views.InstructorUpdateView.as_view(), name='instructor_update'),
    path('instructors/delete/<int:pk>/', views.InstructorDeleteView.as_view(), name='instructor_delete'),
]
