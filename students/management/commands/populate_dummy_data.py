from django.core.management.base import BaseCommand
from students.models import Student, Course, Enrollment, Instructor
from faker import Faker
import random
from django.core.exceptions import ValidationError


class Command(BaseCommand):
    help = 'Populate the database with dummy data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Clear existing data
        Student.objects.all().delete()
        Course.objects.all().delete()
        Enrollment.objects.all().delete()
        Instructor.objects.all().delete()

        # Create Courses
        courses = []
        for _ in range(25):
            course = Course(
                course_name=fake.bs(),
                course_code=fake.unique.bothify(text='???###'),
                description=fake.paragraph(nb_sentences=1)
            )
            course.save()
            courses.append(course)
        self.stdout.write(self.style.SUCCESS(f'Created {len(courses)} courses'))

        # Create Instructors
        instructors = []
        for _ in range(15):
            instructor = Instructor(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.unique.email()
            )
            instructor.save()
            instructor.courses.add(*random.sample(courses, random.randint(1, 3)))
            instructors.append(instructor)
        self.stdout.write(self.style.SUCCESS(f'Created {len(instructors)} instructors'))

        # Create Students
        students = []
        for _ in range(50):
            student = Student(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.unique.email(),
                date_of_birth=fake.date_of_birth(minimum_age=18, maximum_age=25)
            )
            student.save()
            students.append(student)
        self.stdout.write(self.style.SUCCESS(f'Created {len(students)} students'))

        # Create Enrollments
        enrollments = []
        for student in students:
            for _ in range(random.randint(1, 5)):
                course = random.choice(courses)
                grade = random.choice(['A', 'A+', 'A-', 'B', 'B+', 'B-', 'C', 'D', 'E', 'F'])
                exam_score = round(random.uniform(0, 100), 2)

                try:
                    enrollment = Enrollment(
                        student=student,
                        course=course,
                        grade=grade,
                        exam_score=exam_score
                    )
                    enrollment.full_clean()  # Validate the enrollment before saving
                    enrollment.save()
                    enrollments.append(enrollment)
                except ValidationError as e:
                    self.stdout.write(self.style.WARNING(f'Validation error: {e}'))
        self.stdout.write(self.style.SUCCESS(f'Created {len(enrollments)} enrollments'))
