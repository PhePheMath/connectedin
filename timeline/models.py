from django.db import models


class Post(models.Model):
    text = models.CharField(max_length=255, null=False)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    creator = models.ForeignKey('perfil.Profile', on_delete=models.CASCADE,
                                related_name='posts')

    def __str__(self):
        return self.text

    def show_time(self):
        return str(self.date)
