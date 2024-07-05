from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile = models.IntegerField()
    id = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'User'

    def __str__(self):
        return self.name

class Task(models.Model):
    TASK_CHOICES = [
        ('Pending', 'Pending'),
        ('Done', 'Done'),
    ]

    task_details = models.TextField(max_length=50)
    task_type = models.CharField(max_length=50, choices=TASK_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.task_details
