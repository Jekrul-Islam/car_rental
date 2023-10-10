from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

from CarRental import settings

image_storage = FileSystemStorage(
    location=u'{0}/profile_pictures/'.format(settings.MEDIA_ROOT),
    base_url=u'{0}profile_pictures/'.format(settings.MEDIA_URL),
)


def image_directory_path(instance, filename):
    return u'{0}'.format(filename)


class patient(models.Model):
    patientID = models.CharField(max_length = 16)
    name = models.CharField(max_length = 60)
    phone = models.CharField(max_length = 20)
    bloodgroup = models.CharField(max_length = 20)
    checkup = models.BooleanField()

# class appointment(models.Model):
#     username=models.ForeignKey(User, on_delete=models.CASCADE)
#     name=models.CharField(max_length=40)
#     doctor=models.CharField(max_length=40)
#     phone = models.CharField(max_length = 20)
#     date=models.CharField(max_length = 20)
#     time=models.CharField(max_length = 20,unique="True")
#     symtoms=models.CharField(max_length = 50)
#     id = models.IntegerField(primary_key=True)
#
#     def __str__(self):
#         return self.name


class contact(models.Model):
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    phone = models.CharField(max_length = 20)
    gender=models.CharField(max_length = 20)
    comments=models.CharField(max_length = 60)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_name = models.CharField(max_length = 20)
    company = models.CharField(max_length=20)
    color = models.CharField(max_length = 10)
    capacity = models.CharField(max_length = 2)
    is_available = models.BooleanField(default = True)
    description = models.CharField(max_length = 100)
    # car_image = models.ImageField(default='default.jpg', upload_to=image_directory_path, storage=image_storage)

    def __str__(self):
        return self.car_name


class appointment(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)
