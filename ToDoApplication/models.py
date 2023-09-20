from django.db import models

class todo(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    priority = models.IntegerField(default=1)
    is_done = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'todos'