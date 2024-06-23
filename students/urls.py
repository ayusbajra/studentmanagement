from django.urls import path
from django.contrib.auth import views as auth_views
from . import views, views_student, views_course, views_enrollment, views_instructor

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('students/', views_student.StudentListView.as_view(), name='student_list'),
    path('students/<int:pk>/', views_student.StudentDetailView.as_view(), name='student_detail'),
    path('students/create/', views_student.StudentCreateView.as_view(), name='student_create'),
    path('students/update/<int:pk>/', views_student.StudentUpdateView.as_view(), name='student_update'),
    path('students/delete/<int:pk>/', views_student.StudentDeleteView.as_view(), name='student_delete'),

    path('courses/', views_course.CourseListView.as_view(), name='course_list'),
    path('courses/<int:pk>/', views_course.CourseDetailView.as_view(), name='course_detail'),
    path('courses/create/', views_course.CourseCreateView.as_view(), name='course_create'),
    path('courses/update/<int:pk>/', views_course.CourseUpdateView.as_view(), name='course_update'),
    path('courses/delete/<int:pk>/', views_course.CourseDeleteView.as_view(), name='course_delete'),

    path('enrollments/', views_enrollment.EnrollmentListView.as_view(), name='enrollment_list'),
    path('enrollments/<int:pk>/', views_enrollment.EnrollmentDetailView.as_view(), name='enrollment_detail'),
    path('enrollments/create/', views_enrollment.EnrollmentCreateView.as_view(), name='enrollment_create'),
    path('enrollments/update/<int:pk>/', views_enrollment.EnrollmentUpdateView.as_view(), name='enrollment_update'),
    path('enrollments/delete/<int:pk>/', views_enrollment.EnrollmentDeleteView.as_view(), name='enrollment_delete'),

    path('instructors/', views_instructor.InstructorListView.as_view(), name='instructor_list'),
    path('instructors/<int:pk>/', views_instructor.InstructorDetailView.as_view(), name='instructor_detail'),
    path('instructors/create/', views_instructor.InstructorCreateView.as_view(), name='instructor_create'),
    path('instructors/update/<int:pk>/', views_instructor.InstructorUpdateView.as_view(), name='instructor_update'),
    path('instructors/delete/<int:pk>/', views_instructor.InstructorDeleteView.as_view(), name='instructor_delete'),
]
