from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	image = models.ImageField(upload_to="post-images/", blank=True)
	title = models.CharField(max_length=50)
	text = models.TextField()
	publication_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title