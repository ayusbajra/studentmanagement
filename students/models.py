from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()

    class Meta:
        db_table = 'student'

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @property
    def courses(self):
        enrollments = Enrollment.objects.filter(student=self.pk)
        courses = [x.course for x in enrollments]
        return courses


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=25, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'course'

    def __str__(self):
        return self.course_name


class Instructor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    courses = models.ManyToManyField(Course, related_name='instructors')

    class Meta:
        db_table = 'instructor'

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)
    exam_score = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    class Meta:
        db_table = 'enrollment'

    def __str__(self):
        return '{} - {}'.format(self.student, self.course)
