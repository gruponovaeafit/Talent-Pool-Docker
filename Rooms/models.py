from django.db import models


# Create your models here.


def image_path(instance, filename):
    return f'rooms/{instance.id}/{filename}'


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    type = models.CharField(max_length=50)
    price = models.IntegerField()
    capacity = models.IntegerField()
    image = models.ImageField(upload_to=image_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "rooms"

    def __str__(self):
        return self.type
