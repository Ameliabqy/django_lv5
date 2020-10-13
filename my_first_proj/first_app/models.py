from django.db import models
#
# class Name(models.Model):
#     first_name = models.CharField(max_length=264)
#     last_name = models.CharField(max_length=264)
#
#     def __str__(self):
#         return self.first_name + ", " + self.last_name

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=264, default='')
    last_name = models.CharField(max_length=264, default='')
    # top_name = models.ForeignKey(Name, on_delete=models.CASCADE,)
    email = models.CharField(max_length=264)
    def __str__(self):
        return self.email
