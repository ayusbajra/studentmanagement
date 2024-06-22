from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy

from .forms import StudentForm, CourseForm, EnrollmentForm, InstructorForm
from .models import Student, Course, Enrollment, Instructor


class HomeView(TemplateView):
    template_name = 'registration/home.html'


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'students/student_list.html'
    ordering = ['first_name']
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(email__icontains=query)
            )
        return queryset


class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = 'students/student_detail.html'


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student_list')


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student_list')


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy('student_list')


class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'students/course_list.html'


class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'students/course_detail.html'


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'students/course_form.html'
    success_url = reverse_lazy('course_list')


class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'students/course_form.html'
    success_url = reverse_lazy('course_list')


class CourseDeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    template_name = 'students/course_confirm_delete.html'
    success_url = reverse_lazy('course_list')


class EnrollmentListView(LoginRequiredMixin, ListView):
    model = Enrollment
    template_name = 'students/enrollment_list.html'


class EnrollmentDetailView(LoginRequiredMixin, DetailView):
    model = Enrollment
    template_name = 'students/enrollment_detail.html'


class EnrollmentCreateView(LoginRequiredMixin, CreateView):
    model = Enrollment
    form_class = EnrollmentForm
    template_name = 'students/enrollment_form.html'
    success_url = reverse_lazy('enrollment_list')


class EnrollmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Enrollment
    form_class = EnrollmentForm
    template_name = 'students/enrollment_form.html'
    success_url = reverse_lazy('enrollment_list')


class EnrollmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Enrollment
    template_name = 'students/enrollment_confirm_delete.html'
    success_url = reverse_lazy('enrollment_list')


class InstructorListView(LoginRequiredMixin, ListView):
    model = Instructor
    template_name = 'students/instructor_list.html'


class InstructorDetailView(LoginRequiredMixin, DetailView):
    model = Instructor
    template_name = 'students/instructor_detail.html'


class InstructorCreateView(LoginRequiredMixin, CreateView):
    model = Instructor
    form_class = InstructorForm
    template_name = 'students/instructor_form.html'
    success_url = reverse_lazy('instructor_list')


class InstructorUpdateView(LoginRequiredMixin, UpdateView):
    model = Instructor
    form_class = InstructorForm
    template_name = 'students/instructor_form.html'
    success_url = reverse_lazy('instructor_list')


class InstructorDeleteView(LoginRequiredMixin, DeleteView):
    model = Instructor
    template_name = 'students/instructor_confirm_delete.html'
    success_url = reverse_lazy('instructor_list')
