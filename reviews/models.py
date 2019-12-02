from django.db import models
from core import models as core_models

# Create your models here.
class Review(core_models.TimeStampedModel):

    """ Review Model Definition """

    review = models.TextField()
    communication = models.IntegerField()
    check_in = models.IntegerField()
    accuracy = models.IntegerField()
    value = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.review} - {self.room}"
