from django.db import models


class Avatar(models.Model):
    file = models.ImageField(upload_to="avatar/")

    def __str__(self):
        return self.name