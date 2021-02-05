from django.db import models


# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=150)
    answer = models.CharField(max_length=150)
    category = models.CharField(max_length=150)


class Choices(models.Model):
    question = models.ForeignKey("Question", related_name="choices" , on_delete=models.CASCADE)
    choice = models.CharField("choice", max_length=50,)
    position = models.IntegerField("position")

    class Meta:
        unique_together = [
            ("question", "choice"),
            ("question", "position")
        ]
        ordering = ("position",)