from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
from django.db.models import IntegerField, CharField

class Profile(models.Model):
    STUDENT = 1
    TEACHER = 2
    SUPERVISOR = 3
    ROLE_CHOICES = (
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
        (SUPERVISOR, 'Supervisor'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

    Phone_number = models.IntegerField(blank=True, null=True)
    roll_number = models.CharField(max_length=255, blank=True, null=True)
    Email = models.CharField(max_length=255, unique=True, blank=True, null=True)
    Date_of_birth = models.DateField(blank=True, null=True)
    Gender_choice = (('M', 'Male'),
                     ("F", 'Female'))
    gender = models.CharField(max_length=2, choices=Gender_choice, blank=True, null=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class College(models.Model):
    College_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.College_name


class Branch(models.Model):
    Branch_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.Branch_name


class Section(models.Model):
    Section_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.Section_name


class Student(models.Model):
    College_name = models.ForeignKey(College, on_delete=models.CASCADE, blank=True, null=True)
    Branch_name = models.ForeignKey(Branch, on_delete=models.CASCADE, blank=True, null=True)
    Section_name = models.ForeignKey(Section, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    First_name = models.CharField(max_length=255, blank=True, null=True)
    Middle_name = models.CharField(max_length=255, blank=True, null=True)
    Last_name = models.CharField(max_length=255, blank=True, null=True)
    Phone_number = models.IntegerField(blank=True, null=True)
    roll_number = models.CharField(max_length=255, blank=True, null=True)
    Email = models.CharField(max_length=255, unique=True, blank=True, null=True)
    Date_of_birth = models.DateField(blank=True, null=True)
    Gender_choice = (('M', 'Male'),
                     ("F", 'Female'))
    gender = models.CharField(max_length=2, choices=Gender_choice, blank=True, null=True)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.First_name

    def __str__(self):
        return self.Middle_name

    def __str__(self):
        return self.Last_name

    def __str__(self):
        return self.Email

    def __str__(self):
        return self.Date_of_birth

    def __str__(self):
        return self.gender


class Faculty(models.Model):
    College_name = models.ForeignKey(College, on_delete=models.CASCADE, blank=True, null=True)
    Branch_name = models.ForeignKey(Branch, on_delete=models.CASCADE, blank=True, null=True)
    Faculty_name = models.CharField(max_length=255,unique=True, blank=True, null=True)
    Qualification = models.CharField(max_length=255, blank=True, null=True)
    Work_Experience = models.CharField(max_length=255, blank=True, null=True)
    Specialization = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.Faculty_name

    def __str__(self):
        return self.Qualification

    def __str__(self):
        return self.Work_Experience

    def __str__(self):
        return self.Specialization
