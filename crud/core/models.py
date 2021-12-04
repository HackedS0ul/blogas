from django.db import models
#NEW
from django.contrib.auth.models import User

POST_STATUS = (
    ('ACTIVE', ('Active')),
    ('INACTIVE', ('Inactive')),
    ('IN-REVIEW', ('In-Review')),
)
class Post(models.Model):
    title = models.CharField(max_length=200)
    short_desc = models.CharField(max_length=250)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(choices=POST_STATUS, default='IN-REVIEW', max_length=9)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
