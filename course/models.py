from django.db import models


# class Courses(models.Model):
#     course_name = models.CharField(max_length=200)
#     description = models.TextField(max_length=250)
#     course_id = models.PositiveIntegerField()
#     course_fee = models.FloatField()


class Info(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    course_id = models.PositiveIntegerField(default=1)
    enquiry = models.TextField(max_length=250)
    recommendation = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name