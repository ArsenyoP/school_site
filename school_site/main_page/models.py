from django.db import models


class about_page(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    link_button = models.CharField(max_length=30, default="")

    def __str__(self):
        return self.title


class global_data(models.Model):
    name = models.CharField(max_length=50, default="")
    counting = models.IntegerField()
    counting_time = models.IntegerField()

    def __str__(self):
        return self.name

class sections(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    link_button = models.CharField(max_length=30, default="")
    image = models.ImageField(upload_to="sections_images")

    def __str__(self):
        return self.title

class gallery(models.Model):
    image = models.ImageField(upload_to="gallery_images")

