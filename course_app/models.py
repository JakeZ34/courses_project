from django.db import models

# Create your models here.


class CourseManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['course_name']) < 5:
            errors['course_name'] = "Course name should be at least 5 characters"
        if len(postData['desc']) < 15:
            errors['desc'] = "Description should be at least 15 characters"
        return errors


class Description(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Course(models.Model):
    name = models.CharField(max_length=55)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.OneToOneField(
        Description, related_name="course", null=True, on_delete=models.CASCADE)
    objects = CourseManager()
