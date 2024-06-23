from django import forms
from .models import Student, Course, Enrollment, Instructor


class SearchForm(forms.Form):
    """
    Form for searching students or courses based on a query ('q' field).
    """
    q = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Search', 'class': 'form-control'})
    )


class CourseFilterForm(SearchForm):
    """
    Form for filtering courses based on a query ('q' field) and selecting a specific course.
    Inherits from SearchForm.
    """
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        required=False,
        empty_label='All Courses',
        widget=forms.Select(attrs={'class': 'form-select'})
    )


class StudentForm(forms.ModelForm):
    """
    Form for creating or updating student records.
    Uses the Student model fields ['first_name', 'last_name', 'email', 'date_of_birth'].
    """
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'date_of_birth']


class CourseForm(forms.ModelForm):
    """
    Form for creating or updating course records.
    Uses the Course model fields ['course_name', 'course_code', 'description'].
    """
    class Meta:
        model = Course
        fields = ['course_name', 'course_code', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }


class InstructorForm(forms.ModelForm):
    """
    Form for creating or updating instructor records.
    Uses the Instructor model fields ['first_name', 'last_name', 'email', 'courses'].
    Allows multiple courses to be selected using checkboxes.
    """
    class Meta:
        model = Instructor
        fields = ['first_name', 'last_name', 'email', 'courses']
        widgets = {
            'courses': forms.CheckboxSelectMultiple,
        }


class EnrollmentForm(forms.ModelForm):
    """
    Form for creating or updating enrollment records.
    Uses the Enrollment model fields ['student', 'course', 'grade', 'exam_score'].
    """
    class Meta:
        model = Enrollment
        fields = ['student', 'course', 'grade', 'exam_score']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-select'}),
            'course': forms.Select(attrs={'class': 'form-select'}),
        }
