from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    likes = models.ImageField(default=0)
    reposts = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return f'/blog/{self.pk}'



class Comment(models.Model):
    date = models.DateTimeField(auto_now=True)
    text = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    def __str__(self):
        return  f'{self.text} {self.blog}'