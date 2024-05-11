from django.db import models

# Create your models here.
class Urls(models.Model):
    id = models.CharField(max_length=7,primary_key=True)
    long_url = models.URLField()
    no_clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} , {self.long_url} ,{self.no_clicks}"