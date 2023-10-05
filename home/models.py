from django.db import models

class Service(models.Model):
  image = models.ImageField(upload_to="images/")
  title = models.CharField(max_length=100)
  description = models.TextField()
  activity =  models.CharField(max_length=100)
  other_activity = models.CharField(max_length=100)
  link = models.URLField(max_length=200, default="http://127.0.0.1:8000/services")

  def __str__(self):
    return self.title