from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from students.forms import EnrollmentForm
from students.models import Enrollment


class EnrollmentListView(LoginRequiredMixin, ListView):
    model = Enrollment
    template_name = 'students/enrollment_list.html'
    ordering = ['student']
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(student__first_name__icontains=query) |
                Q(student__last_name__icontains=query) |
                Q(course__course_name__icontains=query) |
                Q(course__course_code__icontains=query)
            )
        return queryset


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