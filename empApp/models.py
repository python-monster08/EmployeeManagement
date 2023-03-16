from django.db import models

# Create your models here.
class Emp(models.Model):
    name = models.CharField(max_length=100)
    emp_id = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    working = models.BooleanField(default=True)
    department = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    testimonial = models.TextField()
    picture = models.ImageField(upload_to='testimonials/')
    rating = models.IntegerField(max_length=1)

    def __str__(self) -> str:
        return self.testimonial

class Feedback(models.Model):
    email = models.EmailField(('email address'), unique=True)
    name = models.CharField(max_length=100)
    feedback = models.TextField()

    def __str__(self) -> str:
        return self.feedback