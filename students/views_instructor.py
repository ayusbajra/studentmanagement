from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from students.forms import InstructorForm, CourseFilterForm
from students.models import Instructor


class InstructorListView(LoginRequiredMixin, ListView):
    model = Instructor
    template_name = 'students/instructor_list.html'
    ordering = ['first_name']
    paginate_by = 10

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.search_form = None

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.search_form is None:
            self.search_form = CourseFilterForm(self.request.GET)

        if self.search_form.is_valid():
            query = self.search_form.cleaned_data.get('q')
            if query:
                queryset = queryset.filter(
                    Q(first_name__icontains=query) |
                    Q(last_name__icontains=query) |
                    Q(email__icontains=query)
                )

            course = self.search_form.cleaned_data.get('course')
            if course:
                queryset = queryset.filter(courses=course).distinct()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.search_form
        return context


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