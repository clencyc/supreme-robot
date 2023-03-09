from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField()
    age = models.IntegerField()
    course = models.CharField(max_length=50, default='computerscience', blank=False)
    gender = models.CharField(max_length=50, blank=False, null=False)


def __str__(self):
    return self.name


@staticmethod
def get_customer_by_email(email):
    try:
        return Student.objects.get(email=email)
    except:
        return False


def isExists(self):
    if Student.objects.filter(email=self.email):
        return True

    return False




def __str__(self):
    return self.name


