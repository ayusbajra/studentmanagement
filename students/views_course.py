from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from students.forms import CourseForm, SearchForm
from students.models import Course


class CourseListView(LoginRequiredMixin, ListView):
    """
    ListView for displaying a list of courses with optional searching query.
    """
    model = Course
    template_name = 'students/course_list.html'
    ordering = ['course_name']
    paginate_by = 10

    def __init__(self, *args, **kwargs):
        """
        Initializes the EnrollmentListView instance.
        """
        super().__init__(*args, **kwargs)
        self.search_form = None

    def get_queryset(self):
        """
        Returns the queryset of courses filtered by search query.
        """
        queryset = super().get_queryset()

        if self.search_form is None:
            self.search_form = SearchForm(self.request.GET)

        if self.search_form.is_valid():
            query = self.search_form.cleaned_data.get('q')
            if query:
                queryset = queryset.filter(
                    Q(course_name__icontains=query) |
                    Q(course_code__icontains=query)
                )

        return queryset

    def get_context_data(self, **kwargs):
        """
        Adds additional context data to the template context.
        """
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.search_form
        return context


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