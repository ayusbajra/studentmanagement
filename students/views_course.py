from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from students.forms import CourseForm
from students.models import Course


class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'students/course_list.html'
    ordering = ['course_name']
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(course_name__icontains=query) |
                Q(course_code__icontains=query)
            )
        return queryset


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