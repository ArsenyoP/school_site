from django.db import models


class subjects(models.Model):
    subject_name = models.CharField(max_length=64)

    def __str__(self):
        return self.subject_name


class teachers(models.Model):
    name = models.CharField(max_length=32)
    second_name = models.CharField(max_length=32)
    by_father = models.CharField(max_length=32)
    age = models.IntegerField()
    experience =  models.IntegerField()
    subject = models.ManyToManyField(subjects, related_name="teachers")
    education = models.CharField(max_length=128)
    image = models.ImageField(upload_to="teachers_images", default="")

    def __str__(self):
        return f'{self.name,  self.second_name}'



