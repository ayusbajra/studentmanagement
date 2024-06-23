from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from students.forms import StudentForm, CourseFilterForm
from students.models import Student


class StudentListView(LoginRequiredMixin, ListView):
    """
    ListView for displaying a list of students with optional filtering by course and search query.
    """

    model = Student
    template_name = 'students/student_list.html'
    ordering = ['first_name']
    paginate_by = 10

    def __init__(self, *args, **kwargs):
        """
        Initializes the StudentListView instance.
        """
        super().__init__(*args, **kwargs)
        self.search_form = None

    def get_queryset(self):
        """
        Returns the queryset of students filtered by search query and course selection.
        """
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
                queryset = queryset.filter(enrollment__course_id=course).distinct()

        return queryset

    def get_context_data(self, **kwargs):
        """
        Adds additional context data to the template context.
        """
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.search_form
        return context


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