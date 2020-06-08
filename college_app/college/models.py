from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
#3. CollegAdmin : ID, CollegeID (Foreign Key)
#4. College : ID, CollegeName

class AppUser(AbstractUser):
    STUDENT = 1
    TEACHER = 2
    COLLEGEADMIN =3 
    USER_TYPE_CHOICES = (
      (STUDENT, 'student'),
      (TEACHER, 'teacher'),
      (COLLEGEADMIN, 'collegeadmin')
        )
    
    user_type = models.PositiveSmallIntegerField(choices = USER_TYPE_CHOICES,null=True)


class College(models.Model):
    college_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.college_name +": Collge"
    
class Department(models.Model):
    college = models.ForeignKey(College,on_delete="cascade")
    DEPT_TYPE_CHOICES = (
      (1, 'IT'),
      (2, 'ELE'),
      (3, 'MECH')
        )
    dept_type = models.PositiveSmallIntegerField(choices=DEPT_TYPE_CHOICES)

    def __str__(self):
        return str(self.dept_type) + self.college.college_name
    


class CollegeAdmin(models.Model):
    user = models.ForeignKey(AppUser,on_delete="cascade")
    college = models.ForeignKey(College,on_delete="cascade")
    def __str__(self):
        return self.college.college_name + self.user.username
    
    
class Student(models.Model):
    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True
    )
    college = models.OneToOneField(College,on_delete="cascade")
    
    
    # company name
    mother_name = models.CharField(max_length=200, default=None, blank=True, null=True)
    
    department = models.OneToOneField(Department,null=True,on_delete="cascade")


class Teacher(models.Model):
    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True
    )
    college = models.OneToOneField(College,on_delete="cascade")
    
    
    # company name
    department = models.OneToOneField(Department,null=True,on_delete="cascade")