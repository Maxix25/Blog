from django.db import models
from user_profile.models import Profile
from mdeditor.fields import MDTextField

PROGRAMMING = "PROGRAMMING"
PYTHON = "PYTHON"
JAVASCRIPT = "JAVASCRIPT"
CSS = "CSS"
HTML = "HTML"
RUBY = "RUBY"
JAVA = "JAVA"

TOPICS = (
    (CSS, "CSS"),
    (HTML, "HTML"),
    (JAVASCRIPT, "JavaScript"),
    (PYTHON, "Python"),
    (RUBY, "Ruby"),
    (PROGRAMMING, "Programming")
)



# Create your models here.
class Posts(models.Model):
    id = models.AutoField(primary_key = True)
    author = models.ForeignKey(Profile, on_delete = models.CASCADE)
    title = models.CharField(max_length = 30)
    content = MDTextField()
    date = models.DateField(auto_now_add = True)
    topic = models.CharField(
        max_length = 20,
        choices = TOPICS
    )
    def __str__(self):
        return self.title

class Comment(models.Model):
    id = models.AutoField(primary_key = True)
    post = models.ForeignKey(Posts, on_delete = models.CASCADE, related_name = "post")
    name = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name = "name")
    content = models.CharField(max_length = 100)
    date = models.DateField(auto_now_add = True)

    def __str__(self):
        return f"{self.name} - {self.post.title}"


