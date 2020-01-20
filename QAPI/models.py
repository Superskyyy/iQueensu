from django.db import models


# Create your models here.


class QPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=200)
    post_text = models.TextField()
    post_author = models.CharField(max_length=200)
    post_date = models.DateTimeField('date posted')

    def __str__(self):
        return str(self.post_id) + "-" + str(self.post_title)
