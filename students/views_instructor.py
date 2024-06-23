from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from students.forms import InstructorForm
from students.models import Instructor


class InstructorListView(LoginRequiredMixin, ListView):
    model = Instructor
    template_name = 'students/instructor_list.html'
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